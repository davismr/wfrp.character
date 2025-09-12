from wfrp.character.data.careers.careers import CAREER_DATA


def get_career_list(species, with_seafarer=False):  # noqa: C901
    if species in ["Human", "Human (Tilean)"] and with_seafarer is False:
        career_list = HUMAN_CAREERS
    elif species in ["Human", "Human (Tilean)"]:
        career_list = HUMAN_CAREERS_WITH_SEAFARER
    elif species.startswith("Human"):
        career_list = HUMAN_NORSE_CAREERS
    elif species == "Halfling" and with_seafarer is False:
        career_list = HALFLING_CAREERS
    elif species == "Halfling":
        career_list = HALFLING_CAREERS_WITH_SEAFARER
    elif species == "Dwarf" and with_seafarer is False:
        career_list = DWARF_CAREERS
    elif species == "Dwarf":
        career_list = DWARF_CAREERS_WITH_SEAFARER
    elif species == "Dwarf (Norse)":
        career_list = DWARF_CAREERS_WITH_SEAFARER
    elif species == "Gnome":
        career_list = GNOME_CAREERS
    elif species == "High Elf" and with_seafarer is False:
        career_list = HIGH_ELF_CAREERS
    elif species == "High Elf":
        career_list = HIGH_ELF_CAREERS_WITH_SEAFARER
    elif species == "Wood Elf":
        career_list = WOOD_ELF_CAREERS
    else:
        raise NotImplementedError("Invalid species sent to list careers")
    return career_list


def list_careers(species=None, with_seafarer=False):
    if species is None:
        return list(CAREER_DATA.keys())
    return list(get_career_list(species, with_seafarer).values())


def get_career(species, die_roll, with_seafarer=False):
    career_list = get_career_list(species, with_seafarer)
    while True:
        try:
            return career_list[die_roll]
        except KeyError:
            die_roll += 1


HUMAN_CAREERS = {
    1: "Apothecary",
    2: "Engineer",
    3: "Lawyer",
    5: "Nun",
    6: "Physician",
    11: "Priest",
    13: "Scholar",
    14: "Wizard",
    15: "Agitator",
    17: "Artisan",
    19: "Beggar",
    20: "Investigator",
    21: "Merchant",
    23: "Rat Catcher",
    26: "Townsman",
    27: "Watchman",
    28: "Advisor",
    29: "Artist",
    30: "Duellist",
    31: "Envoy",
    32: "Noble",
    35: "Servant",
    36: "Spy",
    37: "Warden",
    38: "Bailiff",
    39: "Hedge Witch",
    40: "Herbalist",
    42: "Hunter",
    43: "Miner",
    44: "Mystic",
    45: "Scout",
    50: "Villager",
    51: "Bounty Hunter",
    52: "Coachman",
    54: "Entertainer",
    56: "Flagellant",
    57: "Messenger",
    58: "Pedlar",
    59: "Road Warden",
    60: "Witch Hunter",
    62: "Boatman",
    63: "Huffer",
    65: "Riverwarden",
    68: "Riverwoman",
    70: "Seaman",
    71: "Smuggler",
    73: "Stevedore",
    74: "Wrecker",
    76: "Bawd",
    77: "Charlatan",
    78: "Fence",
    79: "Grave Robber",
    83: "Outlaw",
    84: "Racketeer",
    87: "Thief",
    88: "Witch",
    90: "Cavalryman",
    92: "Guard",
    93: "Knight",
    94: "Pit Fighter",
    95: "Protagonist",
    99: "Soldier",
    100: "Warrior Priest",
}

HUMAN_CAREERS_WITH_SEAFARER = HUMAN_CAREERS.copy()
HUMAN_CAREERS_WITH_SEAFARER[62] = "Beachcomber"
HUMAN_CAREERS_WITH_SEAFARER[63] = "Chantyman"
HUMAN_CAREERS_WITH_SEAFARER[64] = "Huffer"
HUMAN_CAREERS_WITH_SEAFARER[66] = "Officer"
HUMAN_CAREERS_WITH_SEAFARER[67] = "Sailor-Priest of Manann"
HUMAN_CAREERS_WITH_SEAFARER[71] = "Sailor"
HUMAN_CAREERS_WITH_SEAFARER[73] = "Ship’s Gunner"
HUMAN_CAREERS_WITH_SEAFARER[74] = "Wrecker"
del HUMAN_CAREERS_WITH_SEAFARER[65]
del HUMAN_CAREERS_WITH_SEAFARER[68]
del HUMAN_CAREERS_WITH_SEAFARER[70]

HUMAN_NORSE_CAREERS = {
    2: "Nun",
    4: "Scholar",
    6: "Agitator",
    10: "Artisan",
    12: "Beggar",
    13: "Rat Catcher",
    15: "Merchant",
    18: "Advisor",
    19: "Artist",
    20: "Noble",
    27: "Servant",
    30: "Herbalist",
    34: "Hunter",
    37: "Mystic",
    40: "Scout",
    46: "Villager",
    48: "Entertainer",
    49: "Messenger",
    52: "Pedlar",
    54: "Charlatan",
    57: "Outlaw",
    61: "Thief",
    64: "Witch",
    66: "Beachcomber",
    69: "Huffer",
    77: "Sailor",
    82: "Wrecker",
    85: "Cavalryman",
    89: "Pit Fighter",
    92: "Protagonist",
    100: "Soldier",
}

DWARF_CAREERS = {
    1: "Apothecary",
    4: "Engineer",
    6: "Lawyer",
    7: "Physician",
    9: "Scholar",
    11: "Agitator",
    17: "Artisan",
    18: "Beggar",
    20: "Investigator",
    24: "Merchant",
    25: "Rat Catcher",
    31: "Townsman",
    34: "Watchman",
    36: "Advisor",
    37: "Artist",
    38: "Duellist",
    40: "Envoy",
    41: "Noble",
    42: "Servant",
    43: "Spy",
    45: "Warden",
    47: "Bailiff",
    49: "Hunter",
    54: "Miner",
    55: "Scout",
    56: "Villager",
    60: "Bounty Hunter",
    61: "Coachman",
    63: "Entertainer",
    65: "Messenger",
    67: "Pedlar",
    69: "Boatman",
    70: "Huffer",
    72: "Riverwoman",
    73: "Seaman",
    75: "Smuggler",
    77: "Stevedore",
    78: "Wrecker",
    79: "Fence",
    82: "Outlaw",
    83: "Racketeer",
    84: "Thief",
    87: "Guard",
    90: "Pit Fighter",
    93: "Protagonist",
    96: "Soldier",
    100: "Slayer",
}

DWARF_CAREERS_WITH_SEAFARER = DWARF_CAREERS.copy()
DWARF_CAREERS_WITH_SEAFARER[69] = "Huffer"
DWARF_CAREERS_WITH_SEAFARER[71] = "Officer"
DWARF_CAREERS_WITH_SEAFARER[74] = "Sailor"
DWARF_CAREERS_WITH_SEAFARER[77] = "Ship’s Gunner"
del DWARF_CAREERS_WITH_SEAFARER[70]
del DWARF_CAREERS_WITH_SEAFARER[72]
del DWARF_CAREERS_WITH_SEAFARER[73]
del DWARF_CAREERS_WITH_SEAFARER[75]

HALFLING_CAREERS = {
    1: "Apothecary",
    2: "Engineer",
    4: "Lawyer",
    6: "Physician",
    8: "Scholar",
    10: "Agitator",
    15: "Artisan",
    19: "Beggar",
    21: "Investigator",
    25: "Merchant",
    28: "Rat Catcher",
    31: "Townsman",
    33: "Watchman",
    34: "Advisor",
    36: "Artist",
    37: "Envoy",
    43: "Servant",
    44: "Spy",
    46: "Warden",
    47: "Bailiff",
    50: "Herbalist",
    52: "Hunter",
    53: "Miner",
    54: "Scout",
    57: "Villager",
    58: "Bounty Hunter",
    60: "Coachman",
    63: "Entertainer",
    65: "Messenger",
    67: "Pedlar",
    68: "Road Warden",
    69: "Boatman",
    70: "Huffer",
    71: "Riverwarden",
    74: "Riverwoman",
    75: "Seaman",
    79: "Smuggler",
    82: "Stevedore",
    85: "Bawd",
    86: "Charlatan",
    87: "Fence",
    88: "Grave Robber",
    89: "Outlaw",
    90: "Racketeer",
    94: "Thief",
    96: "Guard",
    97: "Pit Fighter",
    100: "Soldier",
}

HALFLING_CAREERS_WITH_SEAFARER = HALFLING_CAREERS.copy()
HALFLING_CAREERS_WITH_SEAFARER[72] = "Beachcomber"
HALFLING_CAREERS_WITH_SEAFARER[74] = "Huffer"
HALFLING_CAREERS_WITH_SEAFARER[80] = "Sailor"
HALFLING_CAREERS_WITH_SEAFARER[82] = "Ship’s Gunner"
del HALFLING_CAREERS_WITH_SEAFARER[69]
del HALFLING_CAREERS_WITH_SEAFARER[70]
del HALFLING_CAREERS_WITH_SEAFARER[71]
del HALFLING_CAREERS_WITH_SEAFARER[75]
del HALFLING_CAREERS_WITH_SEAFARER[79]

GNOME_CAREERS = {
    1: "Apothecary",
    2: "Lawyer",
    3: "Physician",
    5: "Priest",
    6: "Scholar",
    8: "Wizard",
    15: "Agitator",
    16: "Artisan",
    18: "Beggar",
    19: "Investigator",
    20: "Merchant",
    22: "Rat Catcher",
    23: "Townsman",
    29: "Watchman",
    30: "Advisor",
    31: "Artist",
    32: "Envoy",
    33: "Noble",
    34: "Servant",
    36: "Spy",
    41: "Warden",
    43: "Bailiff",
    44: "Herbalist",
    45: "Hunter",
    47: "Miner",
    55: "Scout",
    59: "Villager",
    63: "Bounty Hunter",
    64: "Entertainer",
    69: "Messenger",
    70: "Pedlar",
    76: "Boatman",
    77: "Riverwoman",
    81: "Smuggler",
    84: "Bawd",
    86: "Charlatan",
    91: "Fence",
    92: "Outlaw",
    93: "Racketeer",
    95: "Thief",
    98: "Guard",
    99: "Soldier",
    100: "Warrior Priest",
}

HIGH_ELF_CAREERS = {
    2: "Apothecary",
    6: "Lawyer",
    8: "Physician",
    12: "Scholar",
    16: "Wizard",
    19: "Artisan",
    21: "Investigator",
    26: "Merchant",
    28: "Townsman",
    29: "Watchman",
    31: "Advisor",
    32: "Artist",
    34: "Duellist",
    37: "Envoy",
    40: "Noble",
    43: "Spy",
    45: "Warden",
    47: "Herbalist",
    50: "Hunter",
    56: "Scout",
    59: "Bounty Hunter",
    62: "Entertainer",
    63: "Messenger",
    64: "Boatman",
    79: "Seaman",
    80: "Smuggler",
    82: "Bawd",
    85: "Charlatan",
    88: "Outlaw",
    92: "Cavalryman",
    94: "Guard",
    95: "Knight",
    97: "Pit Fighter",
    98: "Protagonist",
    100: "Soldier",
}

HIGH_ELF_CAREERS_WITH_SEAFARER = HIGH_ELF_CAREERS.copy()
HIGH_ELF_CAREERS_WITH_SEAFARER[64] = "Chantyman"
HIGH_ELF_CAREERS_WITH_SEAFARER[65] = "Huffer"
HIGH_ELF_CAREERS_WITH_SEAFARER[69] = "Officer"
HIGH_ELF_CAREERS_WITH_SEAFARER[79] = "Sailor"
HIGH_ELF_CAREERS_WITH_SEAFARER[80] = "Ship’s Gunner"

WOOD_ELF_CAREERS = {
    1: "Scholar",
    5: "Wizard",
    10: "Artisan",
    14: "Advisor",
    18: "Artist",
    25: "Envoy",
    31: "Noble",
    35: "Spy",
    42: "Herbalist",
    52: "Hunter",
    57: "Mystic",
    68: "Scout",
    70: "Bounty Hunter",
    75: "Entertainer",
    78: "Messenger",
    79: "Wrecker",
    85: "Outlaw",
    90: "Cavalryman",
    92: "Guard",
    94: "Knight",
    96: "Pit Fighter",
    100: "Soldier",
}
