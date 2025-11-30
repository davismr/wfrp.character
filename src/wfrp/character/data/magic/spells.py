from wfrp.character.data.magic import colour_magic
from wfrp.character.data.magic import colour_winds_of_magic
from wfrp.character.data.magic.arcane import ARCANE_MAGIC_DATA
from wfrp.character.data.magic.arcane_winds_of_magic import ARCANE_WINDS_OF_MAGIC_DATA


def get_arcane_spells(expansions):
    arcane_spells = ARCANE_MAGIC_DATA
    if "winds_of_magic" in expansions:
        arcane_spells.update(ARCANE_WINDS_OF_MAGIC_DATA)
        arcane_spells = dict(sorted(arcane_spells.items()))
    return arcane_spells


def get_colour_spells(lore, expansions):
    lore_title = f"LORE_{lore.upper()}_DATA"
    spells = getattr(colour_magic, lore_title)
    if "winds_of_magic" in expansions:
        spells = spells | getattr(colour_winds_of_magic, lore_title)
        spells = dict(sorted(spells.items()))
    return spells
