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
    old_toughness = new_character.toughness = 40
    request = testing.DummyRequest(
        post={"": {"Toughness": "5"}, "Accept_Advances": "Accept_Advances"}
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.toughness == old_toughness + 5
