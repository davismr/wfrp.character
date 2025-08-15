from datetime import datetime
from datetime import timezone

from freezegun import freeze_time
import pytest

from wfrp.character.application import DBSession
from wfrp.character.data.careers.careers import CAREER_DATA
from wfrp.character.models.character import Character
from wfrp.character.views.create_character.attributes import ATTRIBUTES_LOWER


@pytest.mark.models
def test_save_character(testapp):
    # make sure db is empty
    DBSession.query(Character).delete()
    new_character = Character()
    new_character.name = "Jacob Grimm"
    assert new_character.name == "Jacob Grimm"
    DBSession.add(new_character)
    assert DBSession.query(Character).count() == 1
    character = DBSession.query(Character).first()
    assert character.name == "Jacob Grimm"


@pytest.mark.models
def test_modified(testapp):
    # make sure db is empty
    DBSession.query(Character).delete()
    new_character = Character()
    new_character.name = "Wilhelm Grimm"
    with freeze_time("2024-01-02 03:04:05"):
        DBSession.add(new_character)
        new_charcter = (
            DBSession.query(Character).filter_by(name="Wilhelm Grimm").first()
        )
    assert new_charcter.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_charcter.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_character.name = "Jacob Grimm"
        new_charcter = DBSession.query(Character).filter_by(name="Jacob Grimm").first()
    assert new_charcter.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)


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
    new_character.talents = {"Small": 1}
    assert new_character.calculate_wounds() == 10


@pytest.mark.models
def test_wounds_hardy_halfling(new_character):
    new_character.species = "Halfling"
    new_character.strength_initial = 80
    new_character.toughness_initial = 36
    new_character.willpower_initial = 46
    new_character.talents = {"Hardy": 1, "Small": 1}
    assert new_character.calculate_wounds() == 13


@pytest.mark.models
def test_character_title(new_character):
    assert new_character.get_display_title() == "Unknown"
    assert new_character.get_filename() == "unknown"
    new_character.species = "Halfling"
    assert new_character.get_display_title() == "Halfling"
    assert new_character.get_filename() == "halfling"
    new_character.career = "Bawd"
    assert new_character.get_display_title() == "Halfling Bawd"
    assert new_character.get_filename() == "halfling_bawd"
    new_character.name = "Frodo"
    assert new_character.get_display_title() == "Frodo the Halfling Bawd"
    assert new_character.get_filename() == "frodo_the_halfling_bawd"


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


@pytest.mark.models
@pytest.mark.parametrize(
    "advances, cost",
    [
        (1, 100),
        (2, 200),
        (3, 300),
    ],
)
def test_experience_talent_cost(new_character, advances, cost):
    assert new_character.cost_talent(advances) == cost


@pytest.mark.models
def test_encumberance_trapping(new_character):
    assert new_character.get_encumberance_trapping("Fine Clothing") == 1


@pytest.mark.models
def test_total_encumberance_trappings(complete_character):
    assert complete_character.total_encumberance_trappings() >= 0


@pytest.mark.models
def test_total_encumberance_trappings_fixed(complete_character):
    old_trappings = complete_character.trappings
    complete_character.trappings = ["Fine Clothing", "Cloak", "Backpack"]
    assert complete_character.total_encumberance_trappings() == 4
    complete_character.trappings = old_trappings


@pytest.mark.models
def test_total_encumberance_weapons(complete_character):
    assert complete_character.total_encumberance_weapons() >= 0


@pytest.mark.models
def test_total_encumberance_armour(complete_character):
    assert complete_character.total_encumberance_armour() >= 0


@pytest.mark.models
def test_not_completed_career(complete_character):
    career_data = CAREER_DATA[complete_character.career]
    complete_character.career_title = list(career_data.keys())[0]
    assert complete_character.completed_career() is False


@pytest.mark.models
def test_completed_career(complete_character):
    career_data = CAREER_DATA[complete_character.career]
    complete_character.career_title = list(career_data.keys())[0]
    career_level = career_data[complete_character.career_title]
    for attribute in career_level["attributes"]:
        setattr(
            complete_character, f"{attribute.lower().replace(' ', '_')}_advances", 5
        )
    for skill in career_level["skills"]:
        complete_character.skills[skill] = 5
    complete_character.talents = {career_level["talents"][0]: 1}
    assert complete_character.completed_career() is True


@pytest.mark.models
def test_completed_career_max_level(complete_character):
    complete_character.expansions = ["sea_of_claws"]
    complete_character.career = "Officer"
    complete_character.career_class = "Seafarer"
    complete_character.career_title = "Admiral"
    career_data = complete_character.career_data()
    for _, career_level in career_data.items():
        for attribute in career_level["attributes"]:
            setattr(
                complete_character,
                f"{attribute.lower().replace(' ', '_')}_advances",
                20,
            )
        for skill in career_level["skills"]:
            complete_character.skills[skill] = 20
        complete_character.talents[career_level["talents"][0]] = 1
    assert complete_character.completed_career() is True
    # only need current career level talent
    complete_character.talents = {career_level["talents"][0]: 1}
    assert complete_character.completed_career() is True
    # only need 8 skills
    while len(complete_character.skills) > 8:
        complete_character.skills.popitem()
    assert complete_character.completed_career() is True


@pytest.mark.models
def test_missing_talent(complete_character):
    career_data = CAREER_DATA[complete_character.career]
    complete_character.career_title = list(career_data.keys())[0]
    career_level = career_data[complete_character.career_title]
    for attribute in career_level["attributes"]:
        setattr(
            complete_character, f"{attribute.lower().replace(' ', '_')}_advances", 5
        )
    skills = {}
    for skill in career_level["skills"]:
        skills[skill] = 5
        complete_character.skills = skills
    assert complete_character.completed_career() is False


@pytest.mark.models
def test_missing_skill(complete_character):
    career_data = CAREER_DATA[complete_character.career]
    complete_character.career_title = list(career_data.keys())[0]
    career_level = career_data[complete_character.career_title]
    for attribute in career_level["attributes"]:
        setattr(
            complete_character, f"{attribute.lower().replace(' ', '_')}_advances", 5
        )
    skills = {}
    for skill in career_level["skills"][:-1]:
        skills[skill] = 5
        complete_character.skills = skills
    complete_character.talents = {career_level["talents"][0]: 1}
    assert complete_character.completed_career() is False
    complete_character.skills[career_level["skills"][-1]] = 5
    assert complete_character.completed_career() is True


@pytest.mark.models
def test_missing_attribute(complete_character):
    career_data = CAREER_DATA[complete_character.career]
    complete_character.career_title = list(career_data.keys())[0]
    career_level = career_data[complete_character.career_title]
    for attribute in career_level["attributes"][:-1]:
        setattr(
            complete_character, f"{attribute.lower().replace(' ', '_')}_advances", 5
        )
    skills = {}
    for skill in career_level["skills"]:
        skills[skill] = 5
        complete_character.skills = skills
    complete_character.talents = {career_level["talents"][0]: 1}
    assert complete_character.completed_career() is False
