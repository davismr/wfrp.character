from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.species_data import SPECIES_DATA
from wfrp.character.species_data import SPECIES_LIST
from wfrp.character.views.details import DetailsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    response = view.get_view()
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
