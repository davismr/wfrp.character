from dataclasses import dataclass

from pyramid import testing
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.attributes import ATTRIBUTES
from wfrp.character.views.edit_character import CharacterEditViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.status = "complete"
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="character-edit")
    request.matchdict = {"id": str(new_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)


@pytest.mark.views
def test_expansions(complete_character):
    payload = {
        "__formid__": "expansions_form",
        "expansions": {"expansions": {"sea_of_claws"}},
        "Save_Expansions": "Save_Expansions",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.expansions == ["sea_of_claws"]


@pytest.mark.views
def test_character(complete_character):
    complete_character.species = "Halfling"
    complete_character.career = "Thief"
    payload = {
        "__formid__": "character_form",
        "character": {
            "character_name": "Frodo",
            "experience": "42",
            "experience_spent": "1500",
            "psychology": "Pshychology information",
            "corruption": "Corruption information",
        },
        "Save_Character": "Save_Character",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.get_display_title() == "Frodo the Halfling Thief"
    assert complete_character.experience == 42
    assert complete_character.experience_spent == 1500
    assert complete_character.psychology == "Pshychology information"
    assert complete_character.corruption == "Corruption information"


@pytest.mark.views
def test_career(complete_character):
    complete_character.name = "Frodo"
    complete_character.species = "Halfling"
    complete_character.career = "Apothecary"
    complete_character.career_title = "Foobar"
    payload = {
        "__formid__": "career_form",
        "career": {
            "career": "Thief",
        },
        "Save_Career": "Save_Career",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.get_display_title() == "Frodo the Halfling Thief"
    payload = {
        "__formid__": "career_form",
        "career": {
            "career": "Thief",
            "career_title": "Cat Burglar",
        },
        "Save_Career": "Save_Career",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.get_display_title() == "Frodo the Halfling Thief"
    assert complete_character.career_class == "Rogues"
    assert complete_character.career_title == "Cat Burglar"
    assert complete_character.career_tier == "Silver"
    assert complete_character.career_standing == 1


@pytest.mark.views
def test_species(complete_character):
    complete_character.name = "Frodo"
    complete_character.career = "Thief"
    payload = {
        "__formid__": "species_form",
        "species": {
            "species": "Halfling",
            "movement": "7",
            "fate": "6",
            "fortune": "5",
        },
        "Save_Species": "Save_Species",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.get_display_title() == "Frodo the Halfling Thief"
    assert complete_character.movement == 7
    assert complete_character.fate == 6
    assert complete_character.fortune == 5


@pytest.mark.views
def test_characteristics(complete_character):
    payload = {
        "__formid__": "characteristics_form",
        "characteristics": {},
        "Save_Attributes": "Save_Characteristics",
    }
    for attribute in ATTRIBUTES:
        payload["characteristics"][f"{attribute} Initial"] = "25"
        payload["characteristics"][f"{attribute} Advances"] = "5"
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.intelligence == 30


@pytest.mark.views
def test_skills(complete_character):
    payload = {
        "__formid__": "skills_form",
        "skills": {"add_skill": "Ride"},
        "Save_Skills": "Save_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.skills == {"Ride": 0}
    payload = {
        "__formid__": "skills_form",
        "skills": {
            "Ride": "5",
            "Ride specialisation": "Pegasus",
        },
        "Save_Skills": "Save_Skills",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.skills == {"Ride (Pegasus)": 5}


@pytest.mark.views
def test_talents(complete_character):
    payload = {
        "__formid__": "talents_form",
        "talents": {"add_talent": "Resistance"},
        "Save_Talents": "Save_Talents",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.talents == {"Resistance": 0}
    payload = {
        "__formid__": "talents_form",
        "talents": {
            "Resistance": "1",
            "Resistance specialisation": "Magic",
        },
        "Save_Talents": "Save_Talents",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.talents == {"Resistance (Magic)": 1}


@pytest.mark.views
def test_trappings(complete_character):
    payload = {
        "__formid__": "trappings_form",
        "wealth": {
            "gold_crowns": "5",
            "silver_shillings": "50",
            "brass_pennies": "500",
        },
        "Save_Trappings": "Save_Trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.brass_pennies == 500
    assert complete_character.silver_shillings == 50
    assert complete_character.gold_crowns == 5


@pytest.mark.views
def test_details(complete_character):
    payload = {
        "__formid__": "details_form",
        "details": {
            "eye_colour": "Pale Blue",
            "hair_colour": "Auburn",
            "height": "72",
            "age": "25",
        },
        "Save_Details": "Save_Details",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.eyes == "Pale Blue"
    assert complete_character.hair == "Auburn"
    assert complete_character.height == 72
    assert complete_character.age == 25


@pytest.mark.views
def test_ambitions(complete_character):
    payload = {
        "__formid__": "ambitions_form",
        "ambitions": {
            "short_term_ambition": "My short term ambition",
            "long_term_ambition": "My long term ambition",
        },
        "Save_Ambitions": "Save_Ambitions",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert complete_character.short_term_ambition == "My short term ambition"
    assert complete_character.long_term_ambition == "My long term ambition"


@pytest.mark.views
def test_party(complete_character):
    payload = {
        "__formid__": "party_form",
        "Save_Party": "Save_Party",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
