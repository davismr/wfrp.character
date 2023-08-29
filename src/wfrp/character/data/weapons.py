MELEE_WEAPONS_DATA = {
    "Dagger": {
        "Group": "Basic",
        "Price": {"SS": 16},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
    },
    "Hand Weapon": {
        "Group": "Basic",
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 4],
    },
    "Foil": {
        "Group": "Fencing",
        "Price": {"GC": 5},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Medium",
        "Damage": ["SB", 3],
        "Qualities": ["Fast", "Impale", "Precise", "Undamaging"],
    },
    "Rapier": {
        "Group": "Fencing",
        "Price": {"GC": 5},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Fast", "Impale"],
    },
    "Knuckledusters": {
        "Group": "Brawling",
        "Price": {"SS": 2, "BP": 6},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 2],
    },
    "Flail": {
        "Group": "Flail",
        "Price": {"GC": 2},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Average",
        "Damage": ["SB", 5],
        "Qualities": ["Distract", "Wrap"],
    },
    "Quarterstaff": {
        "Group": "Polearm",
        "Price": {"SS": 3},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Defensive", "Pummel"],
    },
}

RANGED_WEAPONS_DATA = {
    "Crossbow": {
        "Group": "Crossbow",
        "Price": {"GC": 5},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [9],
        "Qualities": ["Reload 1"],
    },
    "Whip": {
        "Group": "Entangling",
        "Price": {"SS": 5},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 60,
        "Damage": ["SB", 9],
        "Qualities": ["Entangle"],
    },
    "Sling": {
        "Group": "Sling",
        "Price": {"SS": 1},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [6],
    },
}

WEAPONS_DATA = {}
WEAPONS_DATA.update(MELEE_WEAPONS_DATA)
WEAPONS_DATA.update(RANGED_WEAPONS_DATA)
