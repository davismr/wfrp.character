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
def test_submit_view(new_character):
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
    request = testing.DummyRequest(post={"Accept_Attributes": "Accept_Attributes"})
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
