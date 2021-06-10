from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.trappings import TrappingsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert "form" in response


@pytest.mark.views
def test_initalise_form(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.initialise_form()
    assert "class_trappings" in response
    assert "Writing Kit" in response["class_trappings"]
    assert "career_trappings" in response
    assert "Healing Draught" in response["career_trappings"]
    assert "money" in response
    assert isinstance(response["money"]["brass pennies"], int)


@pytest.mark.views
def test_money(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view._get_money("Brass", 4)
    assert "brass pennies" in response
    assert response["brass pennies"] >= 4


@pytest.mark.views
def test_submit_view(new_character):
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    payload = {"Choose_trappings": "Choose_trappings"}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "brass pennies" in new_character.wealth
    assert isinstance(new_character.wealth["brass pennies"], int)
    assert "Pestle and Mortar" in new_character.trappings
    assert "Writing Kit" in new_character.trappings


@pytest.mark.xfail
def test_randomise_trappings(new_character, second_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    class_trappings = response["class_trappings"]
    second_character.species = "Wood Elf"
    second_character.career = "Apothecary"
    second_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    second_class_trappings = response["class_trappings"]
    # these should be different in 90% of cases
    assert class_trappings != second_class_trappings
