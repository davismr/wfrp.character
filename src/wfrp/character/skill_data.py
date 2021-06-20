BASIC_SKILL_DATA = {
    "Art": {
        "characteristic": ("dexterity", "Dex"),
    },
    "Athletics": {
        "characteristic": ("agility", "Ag"),
    },
    "Bribery": {
        "characteristic": ("fellowship", "Fel"),
    },
    "Charm": {"characteristic": ("fellowship", "Fel")},
    "Charm Animal": {"characteristic": ("willpower", "WP")},
    "Climb": {"characteristic": ("strength", "S")},
    "Cool": {"characteristic": ("willpower", "WP")},
    "Consume Alcohol": {"characteristic": ("toughness", "T")},
    "Dodge": {"characteristic": ("agility", "Ag")},
    "Drive": {"characteristic": ("agility", "Ag")},
    "Endurance": {"characteristic": ("toughness", "T")},
    "Entertain": {"characteristic": ("fellowship", "Fel")},
    "Gamble": {"characteristic": ("intelligence", "Int")},
    "Gossip": {"characteristic": ("fellowship", "Fel")},
    "Haggle": {"characteristic": ("fellowship", "Fel")},
    "Intimidate": {"characteristic": ("strength", "S")},
    "Intuition": {"characteristic": ("initiative", "I")},
    "Leadership": {"characteristic": ("fellowship", "Fel")},
    "Melee": {"characteristic": ("weapon_skill", "WS")},
    "Navigation": {"characteristic": ("initiative", "I")},
    "Outdoor Survival": {"characteristic": ("intelligence", "Int")},
    "Perception": {"characteristic": ("initiative", "I")},
    "Ride": {"characteristic": ("agility", "Ag")},
    "Row": {"characteristic": ("strength", "S")},
    "Stealth": {"characteristic": ("agility", "Ag")},
}

ADVANCED_SKILL_DATA = {
    "Animal Care": {
        "characteristic": ("intelligence", "Int"),
    },
    "Animal Training": {
        "characteristic": ("intelligence", "Int"),
        "specialisations": ["Demigryph", "Dog", "Horse", "Pegasus", "Pigeon"],
    },
    "Channelling": {
        "characteristic": ("willpower", "WP"),
    },
    "Evaluate": {"characteristic": ("intelligence", "Int")},
    "Heal": {"characteristic": ("intelligence", "Int")},
    "Language": {"characteristic": ("intelligence", "Int")},
    "Lore": {"characteristic": ("intelligence", "Int")},
    "Perform": {"characteristic": ("agility", "Ag")},
    "Pick Lock": {"characteristic": ("dexterity", "Dex")},
    "Play": {"characteristic": ("dexterity", "Dex")},
    "Pray": {"characteristic": ("fellowship", "Fel")},
    "Ranged": {"characteristic": ("ballistic_skill", "BS")},
    "Research": {"characteristic": ("intelligence", "Int")},
    "Sail": {"characteristic": ("agility", "Ag")},
    "Secret Signs": {"characteristic": ("intelligence", "Int")},
    "Set Trap": {"characteristic": ("dexterity", "Dex")},
    "Sleight of Hand": {"characteristic": ("dexterity", "Dex")},
    "Swim": {"characteristic": ("strength", "S")},
    "Track": {"characteristic": ("initiative", "I")},
    "Trade": {
        "characteristic": ("dexterity", "Dex"),
        "specialisations": [
            "Apothecary",
            "Calligrapher",
            "Chandler",
            "Carpenter",
            "Cook",
            "Embalmer",
            "Smith",
            "Tanner",
        ],
    },
}


SKILL_DATA = {**BASIC_SKILL_DATA, **ADVANCED_SKILL_DATA}
