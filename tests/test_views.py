from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.attributes import ATTRIBUTES
from wfrp.character.views.attributes import AttributesViews
from wfrp.character.views.career import CareerViews
from wfrp.character.views.character import CharacterViews
from wfrp.character.views.details import DetailsViews
from wfrp.character.views.new_character import NewCharacterViews
from wfrp.character.views.species import SpeciesViews
from wfrp.character.views.species_skills import SpeciesSkillsViews
from wfrp.character.views.trappings import TrappingsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_passing_view(session_db):
    view = NewCharacterViews(testing.DummyRequest())
    response = view.character_get_view()
    assert response.status_code == 302
    assert "Location" in response.headers


@pytest.mark.views
def test_species_view(new_character):
    request = testing.DummyRequest(path="species")
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.new_species_view()
    assert "species" in response
    assert "species_list" in response
    assert response["species"] not in response["species_list"]


@pytest.mark.views
@pytest.mark.parametrize(
    "species, experience",
    [("Human", 20), ("Halfling", 0)],
)
def test_submit_species_view(new_character, species, experience):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(post={"species": species})
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.submit_species_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == species
    assert new_character.experience == experience


@pytest.mark.views
def test_submit_species_attributes_view(new_character):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(post={"species": "Human"})
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.submit_species_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == "Human"
    assert new_character.fate == 2
    assert new_character.resilience == 1
    assert new_character.extra_points == 3
    assert new_character.movement == 4


@pytest.mark.views
def test_careers_view(new_character):
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
def test_careers_reroll_view(new_character):
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
def test_submit_career_view_single_career(new_character, career_choice, experience):
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


@pytest.mark.views
def test_new_attributes_view(new_character):
    new_character.species = "Human"
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.new_view()
    assert "base_attributes" in response
    assert "bonus_attributes" in response
    expected_total = 0
    for attribute in ATTRIBUTES:
        expected_total += response["base_attributes"][attribute]
    assert response["total_attributes"] == expected_total


@pytest.mark.views
def test_bonus_attributes_view(new_character):
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view._get_bonus_attributes("Human")
    assert len(response) == 10
    for attribute in ATTRIBUTES:
        assert attribute in response
        assert response[attribute] == 20


@pytest.mark.views
def test_submit_attributes_view(new_character):
    new_character.species = "Human"
    new_character.status = {
        "attributes": {
            "Weapon Skill": 21,
            "Ballistic Skill": 22,
            "Strength": 23,
            "Toughness": 24,
            "Initiative": 25,
            "Agility": 26,
            "Dexterity": 27,
            "Intelligence": 28,
            "Willpower": 29,
            "Fellowship": 30,
        }
    }
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.submit_view()
    assert isinstance(response, HTTPFound)
    assert new_character.weapon_skill == 41
    assert new_character.ballistic_skill == 42
    assert new_character.strength == 43
    assert new_character.toughness == 44
    assert new_character.initiative == 45
    assert new_character.agility == 46
    assert new_character.dexterity == 47
    assert new_character.intelligence == 48
    assert new_character.willpower == 49
    assert new_character.fellowship == 50


@pytest.mark.views
def test_species_skills_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.get_view()
    assert "species_skills" in response
    assert "Athletics" in response["species_skills"]
    assert "species_talents" in response
    assert "Rover" in response["species_talents"]


# TODO expand test
@pytest.mark.views
def test_species_skills_submit(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post={"empty": ""})
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.submit_view()
    assert isinstance(response, HTTPFound)


@pytest.mark.views
def test_trappings_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    assert "class_trappings" in response
    assert "Writing Kit" in response["class_trappings"]
    assert "career_trappings" in response
    assert "Healing Draught" in response["career_trappings"]
    assert "money" in response
    assert isinstance(response["money"]["brass pennies"], int)


@pytest.mark.views
def test_trappings_money(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view._get_money("Brass", 4)
    assert "brass pennies" in response
    assert response["brass pennies"] >= 4


@pytest.mark.xfail
def test_randomise_trappings(new_character, second_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    class_trappings = response["class_trappings"]
    second_character.species = "Wood Elf"
    second_character.career = "Apothecary"
    second_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    second_class_trappings = response["class_trappings"]
    # these should be different in 90% of cases
    assert class_trappings != second_class_trappings


@pytest.mark.views
def test_details_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    response = view.get_view()
    assert "age" in response
    assert "height" in response
    assert "hair_colour" in response
    assert "eye_colour" in response
    assert len(response["eye_colour"].split(","))


@pytest.mark.views
def test_character_view(new_character):
    new_character.status = {"character": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.character_get_view()
    assert response
