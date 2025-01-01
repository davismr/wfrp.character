from dataclasses import dataclass
from unittest.mock import patch

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.forms.create.species import SpeciesViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_get_view(new_character):
    request = testing.DummyRequest(path="species")
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert "form" in response
    assert "Wood Elf" in response["form"]
    assert "Choose species" in response["form"]


@pytest.mark.create
@pytest.mark.parametrize(
    "species, roll",
    [
        ("Human", 42),
        ("Halfling", 93),
        ("Dwarf", 98),
        ("High Elf", 99),
        ("Wood Elf", 100),
    ],
)
def test_roll_new_species(new_character, species, roll):
    request = testing.DummyRequest(path="species")
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    with patch("wfrp.character.forms.create.species.roll_d100") as mock_roll:
        mock_roll.return_value = roll
        response = view._roll_new_species()
        assert response == species
        mock_roll.return_value = 101
        with pytest.raises(NotImplementedError):
            view._roll_new_species()


@pytest.mark.create
@pytest.mark.parametrize(
    "species, roll",
    [
        ("Human", 89),
        ("Halfling", 90),
        ("Dwarf", 97),
        ("Gnome", 98),
        ("High Elf", 99),
    ],
)
@patch("wfrp.character.forms.create.species.is_gnome_active")
def test_roll_new_species_gnome(mock_is_gnome_active, new_character, species, roll):
    mock_is_gnome_active.return_value = True
    request = testing.DummyRequest(path="species")
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    with patch("wfrp.character.forms.create.species.roll_d100") as mock_roll:
        mock_roll.return_value = roll
        response = view._roll_new_species()
        assert response == species
        mock_roll.return_value = 101
        with pytest.raises(NotImplementedError):
            view._roll_new_species()


@pytest.mark.create
@pytest.mark.parametrize(
    "species, movement",
    [("Human", 4), ("Halfling", 3), ("Dwarf", 3), ("High Elf", 5)],
)
def test_set_attributes(new_character, species, movement):
    new_character.status = {"species": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    with pytest.raises(NotImplementedError):
        view._set_species_attributes("Not a species")
    view._set_species_attributes(species)
    assert new_character.movement == movement


@pytest.mark.create
@pytest.mark.parametrize(
    "species, experience",
    [("Human", 20), ("Halfling", 0), ("Dwarf", 0), ("High Elf", 0), ("Wood Elf", 0)],
)
def test_submit_view(new_character, species, experience):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(
        post={"species": {"species": species}, "Choose_Species": "Choose_Species"}
    )
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.species == species
    assert new_character.experience == experience


@pytest.mark.create
def test_submit_species(new_character):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(
        post={"species": {"species": "Human"}, "Choose_Species": "Choose_Species"}
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


@pytest.mark.create
def test_submit_invalid_species(new_character):
    new_character.status = {"species": "Human"}
    request = testing.DummyRequest(
        post={"species": {"species": "Cat"}, "Choose_Species": "Choose_Species"}
    )
    request.matched_route = DummyRoute(name="species")
    request.matchdict = {"uuid": new_character.uuid}
    view = SpeciesViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert '"Cat" is not one of' in response["form"]
