import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.views.attributes import ATTRIBUTES
from wfrp.character.views.attributes import AttributesViews
from wfrp.character.views.career import CareerViews
from wfrp.character.views.character import NewCharacterViews
from wfrp.character.views.species import SpeciesViews


@pytest.mark.views
def test_passing_view(session_db):
    view = NewCharacterViews(testing.DummyRequest())
    response = view.character_get_view()
    assert response.status_code == 302
    assert "Location" in response.headers


@pytest.mark.views
def test_species_view(session_db):
    new_character = Character()
    DBSession.add(new_character)
    view = SpeciesViews(testing.DummyRequest())
    response = view.new_species_view()
    assert "result" in response
    assert "species_list" in response
    assert response["result"] not in response["species_list"]


@pytest.mark.views
def test_careers_view(new_character):
    new_character.species = "Wood Elf"
    request = testing.DummyRequest()
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    response = view.new_career_view()
    assert "career_choice" in response
    assert len(response["career_choice"]) == 1
    assert "career_list" in response
    assert response["career_choice"] not in response["career_list"]


@pytest.mark.views
def test_careers_reroll_view(new_character):
    new_character.species = "Human"
    request = testing.DummyRequest()
    request.matchdict = {"uuid": new_character.uuid}
    request.params = {"career_choice": "Soldier"}
    view = CareerViews(request)
    response = view.reroll_career_view()
    assert "career_choice" in response
    assert "Soldier" in response["career_choice"]
    assert len(response["career_choice"]) == 3
    assert "career_list" in response
    assert "Soldier" not in response["career_list"]


@pytest.mark.views
@pytest.mark.parametrize(
    "career_choice, experience",
    [("Soldier", 50), ("Soldier, Seaman, Bawd", 25), ("Bawd", 0)],
)
def test_submit_career_view_single_career(new_character, career_choice, experience):
    new_character.species = "Human"
    request = testing.DummyRequest(
        post={"career_choice": career_choice, "career": "Soldier"}
    )
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    assert new_character.experience == 0
    response = view.submit_career_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == experience


@pytest.mark.views
def test_submit_attributes_view(new_character):
    new_character.species = "Human"
    request = testing.DummyRequest()
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.new_career_view()
    assert "base_attributes" in response
    assert "bonus_attributes" in response
    expected_total = 0
    for attribute in ATTRIBUTES:
        expected_total += response["base_attributes"][attribute]
    assert response["total_attributes"] == expected_total


@pytest.mark.views
def test_bonus_attributes_view(new_character):
    request = testing.DummyRequest()
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view._get_bonus_attributes("Human")
    assert len(response) == 10
    for attribute in ATTRIBUTES:
        assert attribute in response
        assert response[attribute] == 20
