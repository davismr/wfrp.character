from wfrp.character.data.species_norse import NORSE_SPECIES_DATA
from wfrp.character.data.species_standard import STANDARD_SPECIES_DATA
from wfrp.character.data.species_tilean import TILEAN_SPECIES_DATA

SPECIES_DATA = STANDARD_SPECIES_DATA | NORSE_SPECIES_DATA | TILEAN_SPECIES_DATA
STANDARD_SPECIES_LIST = list(STANDARD_SPECIES_DATA.keys())
SPECIES_LIST = list(SPECIES_DATA.keys())


def get_species_list(expansions):
    species_list = STANDARD_SPECIES_LIST.copy()
    if "rough_nights" not in expansions:
        species_list.remove("Gnome")
    if "sea_of_claws" in expansions:
        species_list.extend(NORSE_SPECIES_DATA.keys())
    if "up_in_arms" in expansions:
        species_list.extend(TILEAN_SPECIES_DATA.keys())
    return species_list


def get_hair_colour(species, die_roll):
    hair_colours = SPECIES_DATA[species]["hair_colour"]
    while True:
        try:
            return hair_colours[die_roll]
        except KeyError:
            die_roll += 1


def get_eye_colour(species, die_roll):
    eye_colours = SPECIES_DATA[species]["eye_colour"]
    while True:
        try:
            return eye_colours[die_roll]
        except KeyError:
            die_roll += 1
