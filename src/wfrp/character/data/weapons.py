MELEE_WEAPONS_DATA = {
    "Dagger": {
        "Group": "Basic",
        "Price": {},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
    },
    "Hand Weapon": {
        "Group": "Basic",
        "Price": {},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 4],
    },
    "Foil": {
        "Group": "Fencing",
        "Price": {},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Medium",
        "Damage": ["SB", 3],
        "Qualities": ["Fast", "Impale", "Precise", "Undamaging"],
    },
    "Rapier": {
        "Group": "Fencing",
        "Price": {},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Fast", "Impale"],
    },
    "Knuckledusters": {
        "Group": "Brawling",
        "Price": {},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 2],
    },
    "Flail": {
        "Group": "Flail",
        "Price": {},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Average",
        "Damage": ["SB", 5],
        "Qualities": ["Distract", "Wrap"],
    },
    "Quarterstaff": {
        "Group": "Polearm",
        "Price": {},
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
        "Price": {},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [9],
        "Qualities": ["Reload 1"],
    },
    "Whip": {
        "Group": "Entangling",
        "Price": {},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 60,
        "Damage": ["SB", 9],
        "Qualities": ["Entangle"],
    },
    "Sling": {
        "Group": "Sling",
        "Price": {},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [6],
    },
}

WEAPONS_DATA = {}
WEAPONS_DATA.update(MELEE_WEAPONS_DATA)
WEAPONS_DATA.update(RANGED_WEAPONS_DATA)
