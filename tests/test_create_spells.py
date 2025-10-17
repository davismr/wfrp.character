from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.spells import SpellsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_form_view(new_character):
    new_character.species = "High Elf"
    new_character.career = "Wizard"
    new_character.status = {"spells": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="spells")
    request.matchdict = {"id": str(new_character.id)}
    view = SpellsViews(request)
    response = view.form_view()
    assert "form" in response
    assert "Twitch" in response["form"]


@pytest.mark.create
def test_submit(new_character):
    new_character.species = "High Elf"
    new_character.career = "Wizard"
    new_character.willpower_initial = 34
    new_character.status = {"spells": ""}
    request = testing.DummyRequest(
        post={
            "spells": {"Animal Friend": "true", "Gust": "true", "Rot": "true"},
            "Choose_Spells": "Choose_Spells",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="spells")
    request.matchdict = {"id": str(new_character.id)}
    view = SpellsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.petty_magic == ["Animal Friend", "Gust", "Rot"]


@pytest.mark.create
@pytest.mark.parametrize("willpower", [24, 44])
def test_number_spells(new_character, willpower):
    new_character.species = "High Elf"
    new_character.career = "Wizard"
    new_character.willpower_initial = willpower
    new_character.status = {"spells": ""}
    request = testing.DummyRequest(
        post={
            "spells": {"Animal Friend": "true", "Gust": "true", "Rot": "true"},
            "Choose_Spells": "Choose_Spells",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="spells")
    request.matchdict = {"id": str(new_character.id)}
    view = SpellsViews(request)
    response = view.form_view()
    if willpower == 24:
        assert "<p>You can only select 2 spells</p>" in response["form"]
    else:
        assert "<p>You have to select 4 spells</p>" in response["form"]
