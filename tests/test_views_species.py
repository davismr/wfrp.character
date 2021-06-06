from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.species import SpeciesViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    request = testing.DummyRequest(path="species")
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert "form" in response
    assert "Wood Elf" in response["form"]
    assert "Choose species" in response["form"]


@pytest.mark.views
@pytest.mark.parametrize(
    "species, experience",
    [("Human", 20), ("Halfling", 0)],
)
def test_submit_view(new_character, species, experience):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(
        post={"species_field": species, "Choose_Species": "Choose_Species"}
    )
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == species
    assert new_character.experience == experience


@pytest.mark.views
def test_submit_attributes_view(new_character):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(
        post={"species_field": "Human", "Choose_Species": "Choose_Species"}
    )
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == "Human"
    assert new_character.fate == 2
    assert new_character.resilience == 1
    assert new_character.extra_points == 3
    assert new_character.movement == 4
