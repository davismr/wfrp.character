import pytest

from wfrp.character.data.careers.seafarer import SEAFARER_CLASS_DATA
from wfrp.character.data.careers.tables import get_career
from wfrp.character.data.careers.tables import list_careers
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


@pytest.mark.data
def test_career_data():  # noqa: C901
    # 8 careers per class
    assert len(SEAFARER_CLASS_DATA) == 8
    for career_class in SEAFARER_CLASS_DATA.values():
        # should be 4 career levels
        assert len(career_class) == 4
        level = 1
        for career_level in career_class.values():
            for key, item in career_level.items():
                if key == "status":
                    assert list(item.keys()) == ["tier", "standing"]
                    assert item["tier"] in ["Gold", "Silver", "Brass"]
                    assert isinstance(item["standing"], int)
                elif key == "attributes":
                    if level == 1:
                        assert len(item) == 3
                    else:
                        assert len(item) == 1
                    for attribute in item:
                        assert attribute in ATTRIBUTES
                elif key == "skills":
                    if level == 1:
                        assert len(item) == 10
                    elif level == 2:
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
                        if talent not in [
                            "Magnum Opus",
                            "Warleader",
                            "Public Speaking",
                        ]:
                            assert talent.split(" (")[0] in TALENT_DATA
                elif key == "trappings":
                    # TODO test trappings
                    assert True
                else:
                    assert False, f"Unexpected Key {key}"
            level += 1
