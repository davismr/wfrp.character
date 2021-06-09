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
    assert "Species Skills" in response["form"]
    assert "Athletics" in response["form"]
    assert "Rover" in response["form"]


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
    if species == "Human":
        assert "Savvy" in response["form"]
        assert "Suave" in response["form"]
    else:
        assert "Small" in response["form"]


@pytest.mark.views
def test_species_skills_submit(new_character):
    payload = {
        "species_skills": {
            "Cool": "0",
            "Entertain (Sing)": "0",
            "Evaluate": "0",
            "Language (Eltharin)": "0",
            "Leadership": "0",
            "Melee (Basic)": "0",
            "Navigation": "5",
            "Perception": "5",
            "Play (any one)": "5",
            "Ranged (Bow)": "3",
            "Sail": "3",
            "Swim": "3",
        },
        "species_talents": {
            "Acute Sense (Sight)": "Acute Sense (Sight)",
            "Coolheaded or Savvy": "Coolheaded",
            "Night Vision": "Night Vision",
            "Read/Write": "Read/Write",
            "Second Sight or Sixth Sense": "Second Sight",
        },
        "Choose_Skills": "Choose_Skills",
    }
    new_character.species = "High Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "Cool" not in new_character.skills
    assert new_character.skills["Perception"] == 5
    assert new_character.skills["Swim"] == 3
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
    response = view.initialise_form()
    assert "career_skills" in response
    assert "Heal" in response["career_skills"]
    assert "career_talents" in response
    assert "Concoct" in response["career_talents"]


@pytest.mark.views
def test_career_skills_submit(new_character):
    payload = {
        "career_skills": {
            "Consume Alcohol": "6",
            "Heal": "6",
            "Language (Classical)": "6",
            "Lore (Chemistry)": "6",
            "Lore (Medicine)": "6",
            "Lore (Plants)": "5",
            "Trade (Apothecary)": "6",
            "Trade (Poisoner)": "6",
        },
        "career_talents": {"career_talent": "Concoct"},
        "Choose_Skills": "Choose_Skills",
    }
    new_character.species = "High Elf"
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.talents == ["Concoct"]
    assert new_character.skills["Heal"] == 6
    assert new_character.skills["Lore (Plants)"] == 5


@pytest.mark.views
def test_skills_add_submit(new_character):
    payload = {
        "species_skills": {
            "Cool": "0",
            "Entertain (Sing)": "0",
            "Evaluate": "0",
            "Language (Eltharin)": "0",
            "Leadership": "0",
            "Melee (Basic)": "0",
            "Navigation": "5",
            "Perception": "5",
            "Play (any one)": "5",
            "Ranged (Bow)": "3",
            "Sail": "3",
            "Swim": "3",
        },
        "species_talents": {
            "Acute Sense (Sight)": "Acute Sense (Sight)",
            "Coolheaded or Savvy": "Coolheaded",
            "Night Vision": "Night Vision",
            "Read/Write": "Read/Write",
            "Second Sight or Sixth Sense": "Second Sight",
        },
        "Choose_Skills": "Choose_Skills",
    }
    new_character.species = "High Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.status == {"career_skills": ""}
    payload = {
        "career_skills": {
            "Consume Alcohol": "6",
            "Heal": "6",
            "Language (Classical)": "6",
            "Lore (Chemistry)": "6",
            "Lore (Medicine)": "6",
            "Lore (Plants)": "6",
            "Trade (Apothecary)": "6",
            "Trade (Poisoner)": "6",
        },
        "career_talents": {"career_talent": "Concoct"},
        "Choose_Skills": "Choose_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert new_character.talents == [
        "Acute Sense (Sight)",
        "Coolheaded",
        "Night Vision",
        "Second Sight",
        "Read/Write",
        "Concoct",
    ]
    assert new_character.skills["Swim"] == 3
    assert new_character.skills["Perception"] == 5
