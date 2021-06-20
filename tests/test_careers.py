import pytest

from wfrp.character.career_data import get_career
from wfrp.character.career_data import list_careers


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
