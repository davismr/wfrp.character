from wfrp.character.data.species_norse import NORSE_SPECIES_DATA
from wfrp.character.data.species_standard import STANDARD_SPECIES_DATA
from wfrp.character.data.species_tilean import TILEAN_SPECIES_DATA

SPECIES_DATA = STANDARD_SPECIES_DATA | NORSE_SPECIES_DATA | TILEAN_SPECIES_DATA
STANDARD_SPECIES_LIST = list(STANDARD_SPECIES_DATA.keys())
SPECIES_LIST = list(SPECIES_DATA.keys())


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
