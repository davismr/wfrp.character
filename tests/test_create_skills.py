from dataclasses import dataclass
from unittest.mock import patch

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.forms.create.career_skills import CareerSkillsViews
from wfrp.character.forms.create.species_skills import SpeciesSkillsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_species_skills_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
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
    new_character.status = {"species_skills": ["talent1", "talent2"]}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
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
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    with patch(
        "wfrp.character.forms.create.species_skills.get_random_talent"
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
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
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
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert "You have to select a specialisation for Play (Any)" in response["form"]
    payload["species_skills"]["Specialisation for Play"] = "Lute"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
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
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
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
    new_character.status = {"species_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "You must select 3 skills for 3 advances" in response["form"]
    assert "You must select 3 skills for 5 advances" in response["form"]


@pytest.mark.create
def test_career_skills_view(new_character):
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.initialise_form()
    assert "career_skills" in response
    assert "Heal" in response["career_skills"]
    assert "career_talents" in response
    assert "Concoct" in response["career_talents"]


@pytest.mark.create
def test_form_view(new_character):
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert "form" in response


@pytest.mark.create
def test_career_skills_submit(new_character):
    payload = {
        "career_skills": {
            "Consume Alcohol": "5",
            "Heal": "6",
            "Language (Classical)": "5",
            "Lore (Chemistry)": "6",
            "Lore (Medicine)": "6",
            "Lore (Plants)": "5",
            "Trade (Apothecary)": "7",
            "Trade (Poisoner)": "0",
        },
        "career_talents": {"career_talent": "Concoct"},
        "Choose_Skills": "Choose_Skills",
    }
    new_character.species = "High Elf"
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)


@pytest.mark.create
@pytest.mark.parametrize(
    "skill_level, message",
    (("4", "you have only allocated 39"), ("6", "you have allocated 41")),
)
def test_validation_error(new_character, skill_level, message):
    payload = {
        "career_skills": {
            "Consume Alcohol": skill_level,
            "Heal": "6",
            "Language (Classical)": "5",
            "Lore (Chemistry)": "6",
            "Lore (Medicine)": "6",
            "Lore (Plants)": "5",
            "Trade (Apothecary)": "7",
            "Trade (Poisoner)": "0",
        },
        "career_talents": {"career_talent": "Concoct"},
        "Choose_Skills": "Choose_Skills",
    }
    new_character.species = "High Elf"
    new_character.career = "Apothecary"
    new_character.status = {"career_skills": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert "form" in response
    assert "There was a problem with your submission" in response["form"]
    assert message in response["form"]


@pytest.mark.create
def test_skills_add_submit(new_character):
    payload = {
        "species_skills": {
            "Cool": "0",
            "Entertain (Sing)": "0",
            "Evaluate": "0",
            "Language (Eltharin)": "5",
            "Leadership": "0",
            "Melee (Basic)": "0",
            "Navigation": "5",
            "Perception": "5",
            "Play (Any)": "0",
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
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="species_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = SpeciesSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.status == {"career_skills": ""}
    payload = {
        "career_skills": {
            "Consume Alcohol": "5",
            "Heal": "5",
            "Language (Classical)": "10",
            "Lore (Chemistry)": "0",
            "Lore (Medicine)": "6",
            "Lore (Plants)": "6",
            "Trade (Apothecary)": "6",
            "Trade (Poisoner)": "2",
        },
        "career_talents": {"career_talent": "Concoct"},
        "Choose_Skills": "Choose_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert list(new_character.talents.keys()) == [
        "Acute Sense (Sight)",
        "Coolheaded",
        "Night Vision",
        "Second Sight",
        "Read/Write",
        "Concoct",
    ]
    for talent in new_character.talents:
        assert new_character.talents[talent] == 1
    assert new_character.skills["Swim"] == 3
    assert new_character.skills["Perception"] == 5


@pytest.mark.create
def test_career_skills_any(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Artisan"
    new_character.status = {"career_skills": ""}
    payload = {
        "career_skills": {
            "Athletics": "5",
            "Cool": "5",
            "Consume Alcohol": "10",
            "Dodge": "5",
            "Endurance": "0",
            "Evaluate": "0",
            "Stealth (Urban)": "5",
            "Trade (Any)": "10",
        },
        "career_talents": {"career_talent": "Artistic"},
        "Choose_Skills": "Choose_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "You have to select a specialisation for Trade (Any)" in response["form"]
    payload["career_skills"]["Trade (Any) specialisation"] = "Embalmer"
    payload["career_talents"]["career_talent"] = "Craftsman (Any)"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert '"Craftsman (Any)" is not one of ' in response["form"]
    payload["career_talents"]["career_talent"] = "Craftsman (Calligrapher)"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "Craftsman (Calligrapher)" in new_character.talents
    assert "Evaluate" not in new_character.skills
    assert "Trade (Any)" not in new_character.skills
    assert new_character.skills["Trade (Embalmer)"] == 10


@pytest.mark.create
def test_career_skills_or_fail(new_character):
    new_character.species = "Human"
    new_character.career = "Pedlar"
    new_character.status = {"career_skills": ""}
    payload = {
        "career_skills": {
            "Charm": "5",
            "Endurance": "5",
            "Entertain (Storytelling)": "10",
            "Gossip": "5",
            "Haggle": "0",
            "Intuition": "0",
            "Outdoor Survival": "5",
            "Stealth (Rural or Urban)": "10",
        },
        "career_talents": {"career_talent": "Tinker"},
        "Choose_Skills": "Choose_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert (
        "You have to select a specialisation for Stealth (Rural or Urban)"
        in response["form"]
    )
    payload["career_skills"]["Stealth (Rural or Urban) specialisation"] = "Urban"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career_skills")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerSkillsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "Stealth (Rural or Urban)" not in new_character.skills
    assert new_character.skills["Stealth (Urban)"] == 10
