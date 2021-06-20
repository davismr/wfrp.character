import pytest

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@pytest.mark.models
def test_save_character(session_db):
    new_character = Character()
    new_character.name = "Jacob Grimm"
    assert new_character.name == "Jacob Grimm"
    DBSession.add(new_character)
    assert DBSession.query(Character).count() == 1
    character = DBSession.query(Character).order_by(Character.uid).first()
    assert character.uid == 1
    assert character.name == "Jacob Grimm"


@pytest.mark.models
def test_toughness(new_character):
    new_character.species = "Human"
    new_character.toughness_initial = 36
    new_character.toughness_advances = 5
    assert new_character.toughness == 41


@pytest.mark.models
def test_wounds(new_character):
    new_character.species = "Human"
    new_character.strength_initial = 26
    new_character.toughness_initial = 36
    new_character.willpower_initial = 46
    assert new_character.calculate_wounds() == 12


@pytest.mark.models
def test_wounds_halfling(new_character):
    new_character.species = "Halfling"
    new_character.toughness_initial = 36
    new_character.willpower_initial = 46
    assert new_character.calculate_wounds() == 10


@pytest.mark.models
def test_character_title(new_character):
    assert new_character.get_display_title() == "Unknown"
    new_character.species = "Halfling"
    assert new_character.get_display_title() == "Halfling"
    new_character.career = "Bawd"
    assert new_character.get_display_title() == "Halfling Bawd"
    new_character.name = "Frodo"
    assert new_character.get_display_title() == "Frodo the Halfling Bawd"


@pytest.mark.models
def test_talent_description(new_character):
    description = new_character.get_talent_description("Flee!")
    assert "Your Movement Attribute counts as 1 higher when Fleeing" in description
