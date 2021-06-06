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
    response = view.get_view()
    assert "species" in response
    assert "species_list" in response
    assert response["species"] not in response["species_list"]


@pytest.mark.views
@pytest.mark.parametrize(
    "species, experience",
    [("Human", 20), ("Halfling", 0)],
)
def test_submit_view(new_character, species, experience):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(post={"species": species})
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.submit_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == species
    assert new_character.experience == experience


@pytest.mark.views
def test_submit_attributes_view(new_character):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(post={"species": "Human"})
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.submit_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == "Human"
    assert new_character.fate == 2
    assert new_character.resilience == 1
    assert new_character.extra_points == 3
    assert new_character.movement == 4
