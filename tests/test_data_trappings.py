import pytest

from wfrp.character.data.armour import ARMOUR_DATA
from wfrp.character.data.class_trappings import get_class_trappings
from wfrp.character.data.trappings import TRAPPINGS_DATA
from wfrp.character.data.weapons import WEAPONS_DATA

IGNORE_TRAPPINGS = [
    "Boat",
    "Fishing Net",
    "Flask of Spirits",
    "Found Boots",
    "Hut",
    "Lunch",
    "Rain Hat",
    "String Bag",
    "Wreck Dwelling",
]


def check_item_exists(trapping):
    if trapping in WEAPONS_DATA:
        return True
    if trapping in ARMOUR_DATA:
        return True
    if trapping in TRAPPINGS_DATA:
        return True
    if trapping in IGNORE_TRAPPINGS:
        return True
    return False


@pytest.mark.data
@pytest.mark.parametrize(
    "career_class",
    [
        "Academics",
        "Burghers",
        "Courtiers",
        "Peasants",
        "Rangers",
        "Riverfolk",
        "Rogues",
        "Seafarer",
        "Warriors",
    ],
)
def test_class_trappings(career_class):
    for trapping in get_class_trappings(career_class):
        for trapping in trapping.split(" or "):
            if " ".join(trapping.split()[1:]) in [
                "sheets of Parchment",
                "Matches",
                "Candles",
            ]:
                continue
            assert check_item_exists(trapping)
