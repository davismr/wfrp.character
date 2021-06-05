from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.trappings import TrappingsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_trappings_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    assert "class_trappings" in response
    assert "Writing Kit" in response["class_trappings"]
    assert "career_trappings" in response
    assert "Healing Draught" in response["career_trappings"]
    assert "money" in response
    assert isinstance(response["money"]["brass pennies"], int)


@pytest.mark.views
def test_trappings_money(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view._get_money("Brass", 4)
    assert "brass pennies" in response
    assert response["brass pennies"] >= 4


@pytest.mark.xfail
def test_randomise_trappings(new_character, second_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    class_trappings = response["class_trappings"]
    second_character.species = "Wood Elf"
    second_character.career = "Apothecary"
    second_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.get_view()
    second_class_trappings = response["class_trappings"]
    # these should be different in 90% of cases
    assert class_trappings != second_class_trappings
