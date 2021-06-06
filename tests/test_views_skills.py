from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.career_skills import CareerSkillsViews
from wfrp.character.views.species_skills import SpeciesSkillsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_species_skills_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
#    assert "species_skills" in response
#    assert "Athletics" in response["species_skills"]
#    assert "species_talents" in response
#    assert "Rover" in response["species_talents"]


@pytest.mark.views
@pytest.mark.parametrize("species, expected_talents", (("Human", 5), ("Halfling", 6)))
def test_random_talents(new_character, species, expected_talents):
    new_character.species = species
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
#    assert len(response["species_talents"]) == expected_talents
#    if species == "Human":
#        assert "Savvy" not in response["species_talents"]
#        assert "Suave" not in response["species_talents"]
#        assert "Savvy or Suave" in response["species_talents"]


@pytest.mark.views
def test_species_skills_submit(new_character):
    payload = {
        "Climb": "on",
        "Perception": "5",
        "Track": "3",
        "Hardy or Second Sight": "Second Sight",
        "Night Vision": "Night Vision",
    }
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "Climb" not in new_character.skills
    assert new_character.skills["Perception"] == 5
    assert new_character.skills["Track"] == 3
    assert "Second Sight" in new_character.talents
    assert "Night Vision" in new_character.talents


@pytest.mark.views
def test_career_skills_view(new_character):
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerSkillsViews(request)
    response = view.get_view()
    assert "career_skills" in response
    assert "Heal" in response["career_skills"]
    assert "career_talents" in response
    assert "Concoct" in response["career_talents"]


@pytest.mark.views
def test_career_skills_submit(new_character):
    payload = {"Heal": "6", "Lore (Plants)": "5", "career_talents": "Concoct"}
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerSkillsViews(request)
    response = view.submit_view()
    assert isinstance(response, HTTPFound)
    assert new_character.talents == ["Concoct"]
    assert new_character.skills["Heal"] == 6
    assert new_character.skills["Lore (Plants)"] == 5


@pytest.mark.views
def test_skills_add_submit(new_character):
    payload = {
        "Perception": "5",
        "Track": "3",
        "Hardy or Second Sight": "Second Sight",
        "Night Vision": "Night Vision",
    }
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.status == {"career_skills": ""}
    payload = {"Track": "6", "Perception": "5", "career_talents": "Concoct"}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerSkillsViews(request)
    response = view.submit_view()
    assert new_character.talents == ["Second Sight", "Night Vision", "Concoct"]
    assert new_character.skills["Track"] == 9
    assert new_character.skills["Perception"] == 10
