from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.advances import AdvancesViews


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
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "5", "Dexterity": "0", "Intelligence": "0"},
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
