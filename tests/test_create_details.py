from dataclasses import dataclass
from unittest.mock import patch

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.data.species import SPECIES_DATA
from wfrp.character.data.species import SPECIES_LIST
from wfrp.character.views.create_character.details import DetailsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_initialise_form_elf(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "age" in response
    assert "height" in response
    assert "hair_colour" in response
    assert "eye_colour" in response
    assert len(response["eye_colour"].split(","))


@pytest.mark.create
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.create
@pytest.mark.parametrize("species", SPECIES_LIST)
def test_hair_colour(new_character, species):
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
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


@pytest.mark.create
@pytest.mark.parametrize("species", SPECIES_LIST)
def test_eye_colour(new_character, species):
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
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


@pytest.mark.create
def test_eye_colour_free(new_character):
    new_character.species = "Human"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    with patch("wfrp.character.views.create_character.details.roll_2d10") as mock_roll:
        mock_roll.return_value = 2
        view = DetailsViews(request)
        response = view.form_view()
    assert 'value="Pale Blue"' in response["form"]
    assert new_character.status["details"]["eye_colour"] == ""
    assert new_character.status["details"]["hair_colour"] == "White Blond"
    payload = {
        "character_details": {"eye_colour": "Pale Grey"},
        "Choose_Details": "Choose_Details",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert new_character.eyes == "Pale Grey"


@pytest.mark.create
def test_initialise_invalid_species(new_character):
    new_character.species = "Not a species"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    with pytest.raises(NotImplementedError):
        view.initialise_form()


@pytest.mark.create
@pytest.mark.parametrize("species", SPECIES_LIST)
def test_initialise_form_species(new_character, species):
    new_character.species = species
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    initial_values = view.initialise_form()
    for key in ["age", "eye_colour", "hair_colour", "height"]:
        assert key in initial_values


@pytest.mark.create
def test_details_submit(new_character):
    payload = {
        "Choose_Details": "Choose_Details",
    }
    new_character.species = "High Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
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


@pytest.mark.create
def test_invalid_submit(new_character):
    payload = {
        "character_details": {"age": 42},
        "Choose_Details": "Choose_Details",
    }
    new_character.species = "High Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"id": str(new_character.id)}
    view = DetailsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "Pstruct is not a string" in response["form"]
