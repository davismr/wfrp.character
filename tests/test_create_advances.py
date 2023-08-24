from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.forms.create.advances import AdvancesViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.initialise_form()
    assert "attributes" in response
    assert len(response["attributes"]) == 10
    assert "advances" in response
    assert response["advances"] == ["Toughness", "Dexterity", "Intelligence"]


@pytest.mark.views
def test_submit_view(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    old_toughness = new_character.toughness_initial = 40
    new_character.extra_points = 3
    assert new_character.fate == 0
    assert new_character.fortune == 0
    assert new_character.resilience == 0
    assert new_character.resolve == 0
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "5", "Dexterity": "0", "Intelligence": "0"},
            "fate & resilience": {"fate": "2", "resilience": "1"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.toughness_advances == 5
    assert new_character.toughness == old_toughness + 5
    assert new_character.extra_points == 0
    assert new_character.fate == 2
    assert new_character.fortune == 2
    assert new_character.resilience == 1
    assert new_character.resolve == 1


@pytest.mark.views
def test_invalid_submit_view(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "3", "Dexterity": "2", "Intelligence": "1"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "You can only add a total of 5 advances" in response["form"]


@pytest.mark.views
def test_invalid_fate_submit_view(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.extra_points = 3
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "3", "Dexterity": "2", "Intelligence": "1"},
            "fate & resilience": {"fate": "2", "resilience": "2"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "You can only add a total of 5 advances" in response["form"]


@pytest.mark.views
def test_motivation(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "5", "Dexterity": "0", "Intelligence": "0"},
            "fate & resilience": {"fate": "0", "resilience": "0"},
            "motivation": {"motivation": "Protect the weak"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.motivation == "Protect the weak"


@pytest.mark.views
def test_motivation_not_required(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "5", "Dexterity": "0", "Intelligence": "0"},
            "fate & resilience": {"fate": "0", "resilience": "0"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.motivation == ""
