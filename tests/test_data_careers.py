import pytest

from wfrp.character.data.careers.academics import ACADEMIC_CLASS_DATA
from wfrp.character.data.careers.burghers import BURGHERS_CLASS_DATA
from wfrp.character.data.careers.courtiers import COURTIERS_CLASS_DATA
from wfrp.character.data.careers.peasants import PEASANTS_CLASS_DATA
from wfrp.character.data.careers.rangers import RANGERS_CLASS_DATA
from wfrp.character.data.careers.riverfolk import RIVERFOLK_CLASS_DATA
from wfrp.character.data.careers.rogues import ROGUES_CLASS_DATA
from wfrp.character.data.careers.seafarer import PRIEST_OF_STROMFELS
from wfrp.character.data.careers.seafarer import SEAFARER_CLASS_DATA
from wfrp.character.data.careers.tables import get_career
from wfrp.character.data.careers.tables import list_careers
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CLASS_DATA
from wfrp.character.data.careers.warriors import WARRIORS_CLASS_DATA
from wfrp.character.data.careers.winds_of_magic import WINDS_OF_MAGIC_CLASS_DATA
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.views.create_character.attributes import ATTRIBUTES


@pytest.mark.data
@pytest.mark.parametrize(
    "species, career",
    [
        ("Human", "Hunter"),
        ("Dwarf", "Servant"),
        ("Halfling", "Servant"),
        ("High Elf", "Spy"),
        ("Wood Elf", "Herbalist"),
    ],
)
def test_get_career(species, career):
    random_career = get_career(species, 42)
    assert random_career == career


@pytest.mark.data
@pytest.mark.parametrize(
    "species, career",
    [
        ("Human", "Sailor"),
        ("Dwarf", "Officer"),
        ("Halfling", "Beachcomber"),
        ("High Elf", "Sailor"),
        ("Wood Elf", "Entertainer"),
    ],
)
def test_get_career_seafarer(species, career):
    random_career = get_career(species, 71, True)
    assert random_career == career


@pytest.mark.data
def test_get_career_invalid():
    with pytest.raises(NotImplementedError):
        get_career("Not a species", 42)


@pytest.mark.data
def test_not_integer():
    with pytest.raises(TypeError):
        get_career("Human", "Not a number")


@pytest.mark.data
def test_list_careers():
    careers = list_careers()
    assert len(careers) == 64


@pytest.mark.data
def test_list_human_careers():
    careers = list_careers("Human")
    assert len(careers) == 63
    assert "Slayer" not in careers


@pytest.mark.data
def test_list_dwarf_careers():
    careers = list_careers("Dwarf")
    assert len(careers) == 47
    assert "Slayer" in careers
    assert "Knight" not in careers


@pytest.mark.data
def test_list_halfling_careers():
    careers = list_careers("Halfling")
    assert len(careers) == 48
    assert "Slayer" not in careers
    assert "Road Warden" in careers


@pytest.mark.data
def test_list_high_elf_careers():
    careers = list_careers("High Elf")
    assert len(careers) == 35
    assert "Slayer" not in careers
    assert "Knight" in careers
    assert "Smuggler" in careers


@pytest.mark.data
def test_list_wood_elf_careers():
    careers = list_careers("Wood Elf")
    assert len(careers) == 22
    assert "Slayer" not in careers
    assert "Wrecker" in careers


@pytest.mark.data
def test_list_careers_invalid():
    with pytest.raises(NotImplementedError):
        list_careers("Not a species")


def assert_career_level(career, career_name, career_level, level):  # noqa: C901
    for key, item in career_level.items():
        if key == "status":
            assert list(item.keys()) == ["tier", "standing"]
            assert item["tier"] in ["Gold", "Silver", "Brass"]
            assert isinstance(item["standing"], int)
            if career in ["Pauper", "Zealot"]:
                assert item["standing"] == 0
            else:
                assert item["standing"] > 0
        elif key == "attributes":
            if level == 1:
                assert len(item) == 3
            else:
                assert len(item) == 1
            for attribute in item:
                assert attribute in ATTRIBUTES
        elif key == "skills":
            if level == 1:
                assert len(item) in [8, 10]
            elif level == 2:
                if career_name in ["Freelance", "Knight of the Blazing Sun"]:
                    assert len(item) == 7
                else:
                    assert len(item) == 6
            elif level == 3:
                assert len(item) == 4
            elif level == 4:
                assert len(item) == 2
            for skill in item:
                assert skill.split(" (")[0] in SKILL_DATA
        elif key == "talents":
            assert len(item) == 4
            for talent in item:
                assert talent.split(" (")[0] in TALENT_DATA, talent
        elif key == "trappings":
            # TODO test trappings
            assert True
        else:
            assert False, f"Unexpected Key {key}"


@pytest.mark.data
@pytest.mark.parametrize(
    "career_data",
    [
        ACADEMIC_CLASS_DATA,
        BURGHERS_CLASS_DATA,
        COURTIERS_CLASS_DATA,
        PEASANTS_CLASS_DATA,
        RANGERS_CLASS_DATA,
        RIVERFOLK_CLASS_DATA,
        ROGUES_CLASS_DATA,
        SEAFARER_CLASS_DATA,
        WARRIORS_CLASS_DATA,
    ],
)
def test_basic_career_data(career_data):
    # 8 careers per class
    assert len(career_data) == 8
    for career_name, career_class in career_data.items():
        # should be 4 career levels
        assert len(career_class) == 4
        level = 1
        for career, career_level in career_class.items():
            assert_career_level(career, career_name, career_level, level)
            level += 1


@pytest.mark.data
@pytest.mark.parametrize(
    "career_data",
    [
        PRIEST_OF_STROMFELS,
        UP_IN_ARMS_CLASS_DATA,
        WINDS_OF_MAGIC_CLASS_DATA,
    ],
)
def test_career_data(career_data):
    for career_name, career_class in career_data.items():
        # should be 4 career levels
        assert len(career_class) == 4
        level = 1
        for career, career_level in career_class.items():
            assert career, f"Missing career title in {list(career_class.keys())[1]}"
            assert_career_level(career, career_name, career_level, level)
            level += 1
