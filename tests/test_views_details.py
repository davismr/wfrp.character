from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.species_data import SPECIES_DATA
from wfrp.character.species_data import SPECIES_LIST
from wfrp.character.views.details import DetailsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_initialise_form(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    response = view.initialise_form()
    assert "age" in response
    assert "height" in response
    assert "hair_colour" in response
    assert "eye_colour" in response
    assert len(response["eye_colour"].split(","))


@pytest.mark.views
@pytest.mark.parametrize("species", SPECIES_LIST)
def test_hair_colour(new_character, species):
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    hair_colour = view._get_hair_colour(species)
    assert hair_colour in SPECIES_DATA[species]["hair_colour"].values()
    for i in range(100):
        new_hair_colour = view._get_hair_colour(species)
        assert new_hair_colour in SPECIES_DATA[species]["hair_colour"].values()
        if new_hair_colour != hair_colour:
            break
    else:
        raise AssertionError


@pytest.mark.views
@pytest.mark.parametrize("species", SPECIES_LIST)
def test_eye_colour(new_character, species):
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    eye_colour = view._get_eye_colour(species)
    assert eye_colour in SPECIES_DATA[species]["eye_colour"].values()
    for i in range(100):
        new_eye_colour = view._get_eye_colour(species)
        assert new_eye_colour in SPECIES_DATA[species]["eye_colour"].values()
        if new_eye_colour != eye_colour:
            break
    else:
        raise AssertionError


@pytest.mark.views
def test_details_submit(new_character):
    payload = {
        "Choose_Details": "Choose_Details",
    }
    new_character.species = "High Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    initial_values = view.initialise_form()
    stored_values = new_character.status["details"]
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert initial_values == stored_values
    assert new_character.eyes == initial_values["eye_colour"]
    assert new_character.hair == initial_values["hair_colour"]
    assert new_character.height == initial_values["height"]
    assert new_character.age == initial_values["age"]
