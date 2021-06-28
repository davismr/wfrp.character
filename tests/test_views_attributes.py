from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.attributes import ATTRIBUTES
from wfrp.character.views.attributes import AttributesViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Human"
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.initialise_form()
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
def test_bonus_attributes_halfling(new_character):
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view._get_bonus_attributes("Halfling")
    assert len(response) == 10
    assert response["Ballistic Skill"] == 30
    assert response["Willpower"] == 10


@pytest.mark.views
def test_bonus_attributes_dwarf(new_character):
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view._get_bonus_attributes("Dwarf")
    assert len(response) == 10
    assert response["Agility"] == 10
    assert response["Willpower"] == 40


@pytest.mark.views
def test_bonus_attributes_elf(new_character):
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view._get_bonus_attributes("High Elf")
    assert len(response) == 10
    assert response["Intelligence"] == 30
    assert response["Initiative"] == 40


@pytest.mark.views
def test_bonus_attributes_invalid(new_character):
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    with pytest.raises(NotImplementedError):
        view._get_bonus_attributes("Not a species")


@pytest.mark.views
def test_submit_full_experience(new_character):
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
    payload = {
        "attributes": {
            "Weapon Skill": "21",
            "Ballistic Skill": "22",
            "Strength": "23",
            "Toughness": "24",
            "Initiative": "25",
            "Agility": "26",
            "Dexterity": "27",
            "Intelligence": "28",
            "Willpower": "27",
            "Fellowship": "28",
        },
        "Accept_Attributes": "Accept_Attributes",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert (
        "You have used 27 and 28 too many times and not used 29 or 30"
        in response["form"]
    )
    payload["attributes"]["Willpower"] = "29"
    payload["attributes"]["Fellowship"] = "30"
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.weapon_skill_initial == 41
    assert new_character.ballistic_skill_initial == 42
    assert new_character.strength_initial == 43
    assert new_character.toughness_initial == 44
    assert new_character.initiative_initial == 45
    assert new_character.agility_initial == 46
    assert new_character.dexterity_initial == 47
    assert new_character.intelligence_initial == 48
    assert new_character.willpower_initial == 49
    assert new_character.fellowship_initial == 50
    assert new_character.experience == 50


@pytest.mark.views
def test_submit_rearrange(new_character):
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
    payload = {
        "attributes": {
            "Weapon Skill": "22",
            "Ballistic Skill": "21",
            "Strength": "30",
            "Toughness": "29",
            "Initiative": "25",
            "Agility": "26",
            "Dexterity": "27",
            "Intelligence": "28",
            "Willpower": "24",
            "Fellowship": "23",
        },
        "Accept_Attributes": "Accept_Attributes",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.weapon_skill_initial == 42
    assert new_character.ballistic_skill_initial == 41
    assert new_character.strength_initial == 50
    assert new_character.toughness_initial == 49
    assert new_character.initiative_initial == 45
    assert new_character.agility_initial == 46
    assert new_character.dexterity_initial == 47
    assert new_character.intelligence_initial == 48
    assert new_character.willpower_initial == 44
    assert new_character.fellowship_initial == 43
    assert new_character.experience == 25


@pytest.mark.views
def test_reroll(new_character):
    new_character.species = "Dwarf"
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest(
        post={
            "Reroll_Attributes": "Reroll_Attributes",
        }
    )
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.initialise_form()
    assert "reroll" not in new_character.status
    attributes = new_character.status["attributes"]
    response = view._reroll()
    assert new_character.status["attributes"] != attributes
    attributes = new_character.status["attributes"]
    assert "reroll" in new_character.status
    response = view._reroll()
    assert new_character.status["attributes"] == attributes
    assert "reroll" in new_character.status
    payload = {
        "attributes": {},
        "Accept_Attributes": "Accept_Attributes",
    }
    for attribute in attributes:
        payload["attributes"][attribute] = str(attributes[attribute])
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == 0


@pytest.mark.views
def test_reroll_submit(new_character):
    new_character.species = "Dwarf"
    new_character.status = {"attributes": ""}
    payload = {
        "Reroll_Attributes": "Reroll_Attributes",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    attributes = new_character.status["attributes"]
    assert "reroll" in new_character.status
    payload = {
        "attributes": {},
        "Accept_Attributes": "Accept_Attributes",
    }
    for attribute in attributes:
        payload["attributes"][attribute] = str(attributes[attribute])
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == 0


@pytest.mark.views
def test_choose_submit(new_character):
    new_character.species = "Human"
    new_character.status = {"attributes": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert "form" in response
    payload = {"Choose_Attributes": "Choose_Attributes"}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert "form" in response
    payload["attributes"] = {}
    payload["attributes"]["Weapon Skill"] = "1"
    payload["attributes"]["Ballistic Skill"] = "20"
    payload["attributes"]["Strength"] = "6"
    payload["attributes"]["Toughness"] = "14"
    payload["attributes"]["Initiative"] = "13"
    payload["attributes"]["Agility"] = "7"
    payload["attributes"]["Dexterity"] = "8"
    payload["attributes"]["Intelligence"] = "9"
    payload["attributes"]["Willpower"] = "11"
    payload["attributes"]["Fellowship"] = "12"
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert "Must be a minimum of 4" in response["form"]
    assert "Must be a maximum of 18" in response["form"]
    payload["attributes"]["Weapon Skill"] = "5"
    payload["attributes"]["Ballistic Skill"] = "17"
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert "Total must be 100, total is currently 102" in response["form"]
    payload["attributes"]["Ballistic Skill"] = "15"
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.weapon_skill_initial == 25
    assert new_character.ballistic_skill_initial == 35
    assert new_character.strength_initial == 26
    assert new_character.toughness_initial == 34
    assert new_character.initiative_initial == 33
    assert new_character.agility_initial == 27
    assert new_character.dexterity_initial == 28
    assert new_character.intelligence_initial == 29
    assert new_character.willpower_initial == 31
    assert new_character.fellowship_initial == 32
    assert new_character.experience == 0
