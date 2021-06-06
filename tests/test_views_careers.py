from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.career import CareerViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"career": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    response = view.new_career_view()
    assert "career_choice" in response
    assert len(response["career_choice"]) == 1
    assert "career_list" in response
    assert response["career_choice"] not in response["career_list"]


@pytest.mark.views
def test_reroll_view(new_character):
    new_character.species = "Human"
    new_character.status = {"career": "Soldier"}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
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
def test_submit_experience(new_character, career_choice, experience):
    new_character.species = "Human"
    new_character.status = {"career": career_choice}
    request = testing.DummyRequest(
        post={"career_choice": career_choice, "career": "Soldier"}
    )
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    assert new_character.experience == 0
    response = view.submit_career_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == experience
