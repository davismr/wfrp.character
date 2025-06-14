from dataclasses import dataclass
from unittest.mock import patch

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.data.class_trappings import get_class_trappings
from wfrp.character.forms.create.trappings import TrappingsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_initalise_form(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "class_trappings" in response
    assert "Writing Kit" in response["class_trappings"]
    assert "career_trappings" in response
    assert "Healing Draught" in response["career_trappings"]
    assert "money" in response
    assert isinstance(response["money"]["brass pennies"], int)


@pytest.mark.create
def test_initalise_form_return(new_character):
    new_character.status = {"trappings": "foobar"}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.initialise_form()
    assert response == "foobar"


@pytest.mark.create
def test_get_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.create
def test_money(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view._get_money("Brass", 2)
    assert "brass pennies" in response
    assert response["brass pennies"] >= 4
    assert response["brass pennies"] <= 40
    response = view._get_money("Silver", 2)
    assert response["silver shillings"] >= 2
    assert response["silver shillings"] <= 20
    response = view._get_money("Gold", 2)
    assert response == {"Gold crown": 2}
    with pytest.raises(NotImplementedError) as error:
        view._get_money("Bronze", 5)
    assert str(error.value) == "Bronze is not defined"


@pytest.mark.create
def test_submit_view(new_character):
    new_character.career = "Protagonist"
    new_character.status = {"trappings": ""}
    payload = {
        "class_trappings": {
            "Clothing": "Clothing",
            "Hand Weapon": "Hand Weapon",
            "Dagger": "Dagger",
            "Pouch": "Pouch",
        },
        "career_trappings": {
            "Hood or Mask": "Mask",
            "Knuckledusters": "Knuckledusters",
            "Leather Jack": "Leather Jack",
        },
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "brass pennies" in new_character.wealth
    assert isinstance(new_character.wealth["brass pennies"], int)
    assert new_character.weapons == ["Dagger", "Hand Weapon", "Knuckledusters"]
    assert new_character.armour == ["Leather Jack"]
    assert new_character.trappings == [
        "Clothing",
        "Dagger",
        "Hand Weapon",
        "Knuckledusters",
        "Leather Jack",
        "Mask",
        "Pouch",
    ]


@pytest.mark.create
def test_submit_artist(new_character):
    new_character.career = "Artist"
    new_character.status = {"trappings": ""}
    payload = {
        "class_trappings": {
            "Dagger": "Dagger",
            "Fine Clothing": "Fine Clothing",
            "Pouch": "Pouch",
            "Tweezers": "Tweezers",
            "Ear Pick": "Ear Pick",
            "Comb": "Comb",
        },
        "career_trappings": {
            "Brush or Chisel or Quill Pen": "Quill Pen",
        },
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "silver shillings" in new_character.wealth
    assert isinstance(new_character.wealth["silver shillings"], int)
    assert new_character.weapons == ["Dagger"]
    assert new_character.armour == []
    assert new_character.trappings == [
        "Comb",
        "Dagger",
        "Ear Pick",
        "Fine Clothing",
        "Pouch",
        "Quill Pen",
        "Tweezers",
    ]


@pytest.mark.create
@patch("wfrp.character.data.class_trappings.roll_d10")
def test_submit_bawd(mock_rolld10, new_character):
    mock_rolld10.return_value = 7
    new_character.career = "Bawd"
    new_character.status = {"trappings": ""}
    class_trappings = {x: x for x in get_class_trappings("Rogues")}
    class_trappings["Hood or Mask"] = "Hood"
    payload = {
        "class_trappings": class_trappings,
        "career_trappings": {
            "Flask of Spirits": "Flask of Spirits",
        },
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "brass pennies" in new_character.wealth
    assert isinstance(new_character.wealth["brass pennies"], int)
    assert new_character.weapons == ["Dagger", "Sling"]
    assert new_character.armour == []
    assert "Hood" in new_character.trappings


@pytest.mark.create
def test_submit_item_with_space(new_character):
    new_character.career = "Road Warden"
    new_character.status = {"trappings": ""}
    payload = {
        "class_trappings": {
            "Backpack": "Backpack",
            "Blanket": "Blanket",
            "Cloak": "Cloak",
            "Clothing": "Clothing",
            "Dagger": "Dagger",
            "Pouch": "Pouch",
            "Rations (1 day)": "Rations (1 day)",
            "Tinderbox": "Tinderbox",
        },
        "career_trappings": {
            "Crossbow with 10 Bolts": "Crossbow with 10 Bolts",
            "Leather Jack": "Leather Jack",
        },
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "brass pennies" in new_character.wealth
    assert isinstance(new_character.wealth["brass pennies"], int)
    assert new_character.weapons == ["Crossbow", "Dagger"]
    assert new_character.armour == ["Leather Jack"]
    assert "Crossbow with 10 Bolts" in new_character.trappings


@pytest.mark.create
def test_submit_view_duplicate_item(new_character):
    new_character.career = "Soldier"
    new_character.status = {"trappings": ""}
    payload = {
        "class_trappings": {
            "Clothing": "Clothing",
            "Hand Weapon": "Hand Weapon",
            "Dagger": "Dagger",
            "Pouch": "Pouch",
        },
        "career_trappings": {
            "Dagger": "Dagger",
            "Leather Breastplate": "Leather Breastplate",
            "Uniform": "Uniform",
        },
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert "silver shillings" in new_character.wealth
    assert isinstance(new_character.wealth["silver shillings"], int)
    assert new_character.weapons == ["Dagger", "Hand Weapon"]
    assert new_character.armour == ["Leather Breastplate"]
    assert new_character.trappings == [
        "Clothing",
        "Dagger",
        "Hand Weapon",
        "Leather Breastplate",
        "Pouch",
        "Uniform",
    ]


@pytest.mark.create
def test_submit_invalid(new_character):
    new_character.career = "Soldier"
    new_character.status = {"trappings": ""}
    payload = {
        "class_trappings": {},
        "career_trappings": {},
        "Choose_trappings": "Choose_trappings",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "There was a problem with your submission" in response["form"]


@pytest.mark.create
@patch("wfrp.character.data.class_trappings.roll_d10")
def test_randomise_trappings(mock_rolld10, new_character, second_character):
    # mock_rolld10.side_effect = [5, 6]
    mock_rolld10.return_value = 5
    new_character.species = "Wood Elf"
    new_character.career = "Apothecary"
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": new_character.uuid}
    view = TrappingsViews(request)
    response = view.initialise_form()
    class_trappings = response["class_trappings"]
    assert "5 sheets of Parchment" in class_trappings
    mock_rolld10.return_value = 6
    second_character.species = "Wood Elf"
    second_character.career = "Apothecary"
    second_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="trappings")
    request.matchdict = {"uuid": second_character.uuid}
    view = TrappingsViews(request)
    response = view.initialise_form()
    second_class_trappings = response["class_trappings"]
    assert "6 sheets of Parchment" in second_class_trappings
    assert class_trappings != second_class_trappings
