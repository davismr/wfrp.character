from dataclasses import dataclass
from unittest.mock import patch

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.species_skills import SpeciesSkillsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_species_skills_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert "Species Skills" in response["form"]
    assert "Athletics" in response["form"]
    assert "Rover" in response["form"]


@pytest.mark.create
def test_initialise_form_return(new_character):
    new_character.species = "Human"
    new_character.career = "Witch"
    new_character.status = {"species-skills": ["talent1", "talent2"]}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.initialise_form()
    assert response["species_talents"] == [
        "Doomed",
        "Savvy or Suave",
        "talent1",
        "talent2",
    ]


@pytest.mark.create
def test_initialise_form_extra(new_character):
    new_character.species = "Human"
    new_character.career = "Witch"
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    with patch(
        "wfrp.character.views.create_character.species_skills.get_random_talent"
    ) as mock_roll:
        mock_roll.side_effect = ["Savvy", "Mimic", "Mimic", "Hardy", "talent1"]
        response = view.initialise_form()
    assert response["species_talents"] == [
        "Doomed",
        "Savvy or Suave",
        "Mimic",
        "Hardy",
        "talent1",
    ]


@pytest.mark.create
@pytest.mark.parametrize("species, expected_talents", (("Human", 5), ("Halfling", 6)))
def test_random_talents(new_character, species, expected_talents):
    new_character.species = species
    new_character.career = "Apothecary"
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    if species == "Human":
        assert "Savvy" in response["form"]
        assert "Suave" in response["form"]
    else:
        assert "Small" in response["form"]


@pytest.mark.create
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
            "Play (Any)": "5",
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
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert "You have to select a specialisation for Play (Any)" in response["form"]
    payload["species_skills"]["Specialisation for Play"] = "Lute"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "Cool" not in new_character.skills
    assert "Specialisation for Play" not in new_character.skills
    assert new_character.skills["Perception"] == 5
    assert new_character.skills["Swim"] == 3
    assert new_character.skills["Play (Lute)"] == 5
    assert "Second Sight" in new_character.talents
    assert "Night Vision" in new_character.talents


@pytest.mark.create
def test_species_skills_invalid(new_character):
    payload = {
        "species_skills": {
            "Cool": "5",
            "Entertain (Sing)": "5",
            "Evaluate": "5",
            "Language (Eltharin)": "5",
            "Leadership": "3",
            "Melee (Basic)": "3",
            "Navigation": "3",
            "Perception": "3",
            "Play (Any)": "0",
            "Ranged (Bow)": "0",
            "Sail": "0",
            "Swim": "0",
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
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "You can only select 3 skills for 3 advances" in response["form"]
    assert "You can only select 3 skills for 5 advances" in response["form"]


@pytest.mark.create
def test_species_skills_invalid_none(new_character):
    payload = {
        "species_skills": {
            "Cool": "0",
            "Entertain (Sing)": "0",
            "Evaluate": "0",
            "Language (Eltharin)": "0",
            "Leadership": "0",
            "Melee (Basic)": "0",
            "Navigation": "0",
            "Perception": "0",
            "Play (Any)": "0",
            "Ranged (Bow)": "0",
            "Sail": "0",
            "Swim": "0",
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
    new_character.status = {"species-skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species-skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "You must select 3 skills for 3 advances" in response["form"]
    assert "You must select 3 skills for 5 advances" in response["form"]
