import pytest

from wfrp.character.data.careers.tables import list_careers
from wfrp.character.data.species import SPECIES_DATA
from wfrp.character.data.species import SPECIES_LIST


@pytest.mark.factories
def test_complete_character(complete_character):
    assert isinstance(complete_character.name, str)
    assert complete_character.species in SPECIES_LIST
    assert complete_character.career in list_careers(complete_character.species)


@pytest.mark.factories
def test_character_factory(character_factory):
    character = character_factory()
    assert isinstance(character.name, str)
    assert character.species in SPECIES_LIST
    assert character.career in list_careers(character.species)
    assert character.hair in SPECIES_DATA[character.species]["hair_colour"].values()
    assert character.eyes in SPECIES_DATA[character.species]["eye_colour"].values()
    # make sure another instance has different attributes
    for i in range(100):
        second_character = character_factory()
        if second_character.species == character.species:
            continue
        assert second_character.career in list_careers(second_character.species)
        assert (
            second_character.hair
            in SPECIES_DATA[second_character.species]["hair_colour"].values()
        )
        assert (
            second_character.eyes
            in SPECIES_DATA[second_character.species]["eye_colour"].values()
        )
        break
    else:
        assert False, f"{i} characters were the same species"
