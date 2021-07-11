import pytest

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.views.attributes import ATTRIBUTES_LOWER


@pytest.mark.models
def test_save_character(session_db):
    # make sure db is empty
    DBSession.query(Character).delete()
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
    new_character.talents = {"Very Resilient": 1}
    assert new_character.toughness == 46


@pytest.mark.models
def test_talents(new_character):
    new_character.species = "Human"
    for attribute in ATTRIBUTES_LOWER:
        setattr(new_character, f"{attribute}_initial", 25)
    for attribute in ATTRIBUTES_LOWER:
        assert getattr(new_character, attribute) == 25
    new_character.talents = {
        "Warrior Born": 1,
        "Marksman": 1,
        "Very Strong": 1,
        "Very Resilient": 1,
        "Sharp": 1,
        "Lightning Reflexes": 1,
        "Nimble Fingered": 1,
        "Savvy": 1,
        "Coolheaded": 1,
        "Suave": 1,
    }
    for attribute in ATTRIBUTES_LOWER:
        assert getattr(new_character, attribute) == 30


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
    description = new_character.get_talent_description("Acute Sense (Taste)")
    assert "One of your primary five senses is highly developed," in description


@pytest.mark.models
@pytest.mark.parametrize(
    "advances, cost",
    [
        (0, 25),
        (9, 30),
        (15, 40),
        (18, 50),
        (25, 70),
        (29, 90),
        (35, 120),
        (36, 150),
        (45, 190),
        (49, 230),
        (54, 280),
        (56, 330),
        (61, 390),
        (70, 450),
        (71, 520),
    ],
)
def test_experience_characteristic_cost(new_character, advances, cost):
    assert new_character.cost_characteristic(advances) == cost


@pytest.mark.models
@pytest.mark.parametrize(
    "advances, cost",
    [
        (0, 10),
        (9, 15),
        (15, 20),
        (18, 30),
        (25, 40),
        (29, 60),
        (35, 80),
        (36, 110),
        (45, 140),
        (49, 180),
        (54, 220),
        (56, 270),
        (61, 320),
        (70, 380),
        (71, 440),
    ],
)
def test_experience_skill_cost(new_character, advances, cost):
    assert new_character.cost_skill(advances) == cost
