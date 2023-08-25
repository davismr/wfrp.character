from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.forms.create.advances import AdvancesViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_initialise_form(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "attributes" in response
    assert len(response["attributes"]) == 10
    assert "advances" in response
    assert response["advances"] == ["Toughness", "Dexterity", "Intelligence"]


@pytest.mark.create
def test_form_view(new_character):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.create
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


@pytest.mark.create
@pytest.mark.parametrize(
    "advance, message",
    (
        ("1", "You have to add a total of 5 advances"),
        ("3", "You can only add a total of 5 advances"),
    ),
)
def test_invalid_submit_view(new_character, advance, message):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": advance, "Dexterity": "2", "Intelligence": "1"},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert message in response["form"]


@pytest.mark.create
@pytest.mark.parametrize("advance", ("1", "3"))
def test_invalid_fate_submit_view(new_character, advance):
    new_character.species = "Human"
    new_character.career = "Apothecary"
    new_character.extra_points = 3
    new_character.status = {"advances": ""}
    request = testing.DummyRequest(
        post={
            "attributes": {"Toughness": "2", "Dexterity": "2", "Intelligence": "1"},
            "fate & resilience": {"fate": "1", "resilience": advance},
            "Accept_Advances": "Accept_Advances",
        }
    )
    request.matched_route = DummyRoute(name="advances")
    request.matchdict = {"uuid": new_character.uuid}
    view = AdvancesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "spread 3 points between fate and resilience" in response["form"]


@pytest.mark.create
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


@pytest.mark.create
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
