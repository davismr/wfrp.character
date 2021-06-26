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
            "Weapon Skill": "Weapon Skill_21",
            "Ballistic Skill": "Ballistic Skill_22",
            "Strength": "Strength_23",
            "Toughness": "Toughness_24",
            "Initiative": "Initiative_25",
            "Agility": "Agility_26",
            "Dexterity": "Dexterity_27",
            "Intelligence": "Intelligence_28",
            "Willpower": "Dexterity_27",
            "Fellowship": "Intelligence_28",
        },
        "Accept_Attributes": "Accept_Attributes",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="attributes")
    request.matchdict = {"uuid": new_character.uuid}
    view = AttributesViews(request)
    response = view.form_view()
    assert (
        "You have used 27 (Dexterity), 28 (Intelligence) more than once"
        in response["form"]
    )
    payload["attributes"]["Willpower"] = "Willpower_29"
    payload["attributes"]["Fellowship"] = "Fellowship_30"
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


@pytest.mark.current
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
            "Weapon Skill": "Ballistic Skill_22",
            "Ballistic Skill": "Weapon Skill_21",
            "Strength": "Fellowship_30",
            "Toughness": "Willpower_29",
            "Initiative": "Initiative_25",
            "Agility": "Agility_26",
            "Dexterity": "Dexterity_27",
            "Intelligence": "Intelligence_28",
            "Willpower": "Toughness_24",
            "Fellowship": "Strength_23",
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
