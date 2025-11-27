BASIC_DATA = {
    "Improvised Weapon": {
        "Group": "Basic",
        "Damage": ["SB", 1],
        "Qualities": ["Undamaging"],
    },
    "Dagger": {
        "Group": "Basic",
        "Price": {"SS": 16},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
    },
    "Knife": {
        "Group": "Basic",
        "Price": {"SS": 8},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 1],
        "Qualities": ["Undamaging"],
    },
    "Hand Weapon": {
        "Group": "Basic",
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 4],
    },
    "Buckler": {
        "Group": "Basic",
        "Price": {"SS": 18, "BP": 2},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 1],
        "Qualities": ["Shield 1", "Defensive", "Undamaging"],
    },
    "Shield": {
        "Group": "Basic",
        "Price": {"GC": 2},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
        "Qualities": ["Shield 2", "Defensive", "Undamaging"],
    },
    "Shield (Large)": {
        "Group": "Basic",
        "Price": {"GC": 3},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Very Short",
        "Damage": ["SB", 3],
        "Qualities": ["Shield 3", "Defensive", "Undamaging"],
    },
}

CAVALRY_DATA = {
    "Cavalry Hammer": {
        "Group": "Cavalry",
        "Price": {"GC": 3},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Two Handed", "Pummel"],
    },
    "Lance": {
        "Group": "Cavalry",
        "Price": {"GC": 1},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": "Very Long",
        "Damage": ["SB", 6],
        "Qualities": ["Impact", "Impale"],
    },
}

FENCING_DATA = {
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
}

BRAWLING_DATA = {
    "Unarmed": {
        "Group": "Brawling",
        "Enc": 0,
        "Reach": "Personal",
        "Damage": ["SB", 0],
        "Qualities": ["Undamaging"],
    },
    "Knuckledusters": {
        "Group": "Brawling",
        "Price": {"SS": 2, "BP": 6},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "Personal",
        "Damage": ["SB", 2],
    },
}

FLAIL_DATA = {
    "Grain Flail": {
        "Group": "Flail",
        "Price": {"SS": 10},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 3],
        "Qualities": ["Distract", "Imprecise", "Wrap"],
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
    "Military Flail": {
        "Group": "Flail",
        "Price": {"GC": 3},
        "Enc": 2,
        "Availability": "Rare",
        "Reach": "Long",
        "Damage": ["SB", 6],
        "Qualities": ["Two Handed", "Distract", "Impact", "Tiring", "Wrap"],
    },
}

PARRY_DATA = {
    "Main Gauche": {
        "Group": "Parry",
        "Price": {"GC": 1},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "Very Short",
        "Damage": ["SB", 2],
        "Qualities": ["Defensive"],
    },
    "Sword-breaker": {
        "Group": "Parry",
        "Price": {"GC": 1, "SS": 2, "BP": 6},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "Short",
        "Damage": ["SB", 3],
        "Qualities": ["Defensive", "Trap-blade"],
    },
}

POLEARM_DATA = {
    "Halberd": {
        "Group": "Polearm",
        "Price": {"GC": 2},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Defensive", "Hack", "Impale"],
    },
    "Spear": {
        "Group": "Polearm",
        "Price": {"SS": 15},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Impale"],
    },
    "Pike": {
        "Group": "Polearm",
        "Price": {"SS": 18},
        "Enc": 4,
        "Availability": "Rare",
        "Reach": "Massive",
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Impale"],
    },
    "Quarterstaff": {
        "Group": "Polearm",
        "Price": {"SS": 3},
        "Enc": 2,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Defensive", "Pummel"],
    },
}

TWO_HANDED_DATA = {
    "Bastard Sword": {
        "Group": "Two Handed",
        "Price": {"GC": 8},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Two Handed", "Damaging", "Defensive"],
    },
    "Great Axe": {
        "Group": "Two Handed",
        "Price": {"GC": 4},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 6],
        "Qualities": ["Two Handed", "Hack", "Impact", "Tiring"],
    },
    "Pick": {
        "Group": "Two Handed",
        "Price": {"SS": 9},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Two Handed", "Damaging", "Impale", "Slow"],
    },
    "Warhammer": {
        "Group": "Two Handed",
        "Price": {"GC": 3},
        "Enc": 3,
        "Availability": "Common",
        "Reach": "Average",
        "Damage": ["SB", 6],
        "Qualities": ["Two Handed", "Damaging", "Pummel", "Slow"],
    },
    "Zweihänder": {
        "Group": "Two Handed",
        "Price": {"GC": 10},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": "Long",
        "Damage": ["SB", 5],
        "Qualities": ["Two Handed", "Damaging", "Hack"],
    },
}

BLACKPOWDER_DATA = {
    "Blunderbuss": {
        "Group": "Blackpowder",
        "Price": {"GC": 2},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": 20,
        "Damage": [8],
        "Qualities": [
            "Two Handed",
            "Blackpowder",
            "Damaging",
            "Blast 3",
            "Dangerous",
            "Reload 2",
        ],
    },
    "Hochland Long Rifle": {
        "Group": "Blackpowder",
        "Price": {"GC": 100},
        "Enc": 3,
        "Availability": "Exotic",
        "Reach": 100,
        "Damage": [9],
        "Qualities": [
            "Two Handed",
            "Blackpowder",
            "Damaging",
            "Accurate",
            "Precise",
            "Reload 4",
        ],
    },
    "Handgun": {
        "Group": "Blackpowder",
        "Price": {"GC": 4},
        "Enc": 2,
        "Availability": "Scarce",
        "Reach": 50,
        "Damage": [9],
        "Qualities": ["Two Handed", "Blackpowder", "Damaging", "Dangerous", "Reload 3"],
    },
    "Pistol": {
        "Group": "Blackpowder",
        "Price": {"GC": 8},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": 20,
        "Damage": [8],
        "Qualities": ["Blackpowder", "Damaging", "Pistol", "Reload 1"],
    },
}

BOW_DATA = {
    "Elf Bow": {
        "Group": "Bow",
        "Price": {"GC": 10},
        "Enc": 2,
        "Availability": "Exotic",
        "Reach": 150,
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Damaging", "Precise"],
    },
    "Longbow": {
        "Group": "Bow",
        "Price": {"GC": 5},
        "Enc": 3,
        "Availability": "Scarce",
        "Reach": 100,
        "Damage": ["SB", 4],
        "Qualities": ["Two Handed", "Damaging"],
    },
    "Bow": {
        "Group": "Bow",
        "Price": {"GC": 4},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 50,
        "Damage": ["SB", 3],
    },
    "Shortbow": {
        "Group": "Bow",
        "Price": {"GC": 3},
        "Enc": 1,
        "Availability": "Common",
        "Reach": 20,
        "Damage": ["SB", 2],
    },
}

CROSSBOW_DATA = {
    "Crossbow Pistol": {
        "Group": "Crossbow",
        "Price": {"GC": 6},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": 10,
        "Damage": [7],
        "Qualities": ["Pistol"],
    },
    "Heavy Crossbow": {
        "Group": "Crossbow",
        "Price": {"GC": 7},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": 100,
        "Damage": [9],
        "Qualities": ["Two Handed", "Damaging", "Reload 1"],
    },
    "Crossbow": {
        "Group": "Crossbow",
        "Price": {"GC": 5},
        "Enc": 2,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [9],
        "Qualities": ["Two Handed", "Reload 1"],
    },
}

ENGINEERING_DATA = {
    "Repeater Handgun": {
        "Group": "Engineering",
        "Price": {"GC": 10},
        "Enc": 3,
        "Availability": "Rare",
        "Reach": 30,
        "Damage": [9],
        "Qualities": ["Two Handed", "Dangerous", "Reload 5", "Repeater 4"],
    },
    "Repeater Pistol": {
        "Group": "Engineering",
        "Price": {"GC": 15},
        "Enc": 1,
        "Availability": "Rare",
        "Reach": 10,
        "Damage": [8],
        "Qualities": ["Dangerous", "Pistol", "Reload 4", "Repeater 4"],
    },
}

ENTANGLING_DATA = {
    "Lasso": {
        "Group": "Entangling",
        "Price": {"SS": 6},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "SB*2",
        "Qualities": ["Entangle"],
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
}

EXPLOSIVES_DATA = {
    "Bomb": {
        "Group": "Explosives",
        "Price": {"GC": 3},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "SB",
        "Damage": [12],
        "Qualities": ["Blast 5", "Dangerous", "Impact"],
    },
    "Incendiary": {
        "Group": "Explosives",
        "Price": {"GC": 1},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": "SB",
        "Damage": "Special",
        "Qualities": ["Blast 4", "Dangerous"],
    },
}

SLING_DATA = {
    "Sling": {
        "Group": "Sling",
        "Price": {"SS": 1},
        "Enc": 0,
        "Availability": "Common",
        "Reach": 60,
        "Damage": [6],
    },
    "Staff Sling": {
        "Group": "Sling",
        "Price": {"SS": 4},
        "Enc": 2,
        "Availability": "Scarce",
        "Reach": 100,
        "Damage": [7],
        "Qualities": ["Two Handed"],
    },
}

THROWING_DATA = {
    "Bolas": {
        "Group": "Throwing",
        "Price": {"SS": 10},
        "Enc": 0,
        "Availability": "Rare",
        "Reach": "SB×3",
        "Damage": ["SB"],
        "Qualities": ["Entangle"],
    },
    "Dart": {
        "Group": "Throwing",
        "Price": {"SS": 2},
        "Enc": 0,
        "Availability": "Scarce",
        "Reach": "SB×2",
        "Damage": ["SB", 1],
        "Qualities": ["Impale"],
    },
    "Javelin": {
        "Group": "Throwing",
        "Price": {"SS": 10, "BP": 6},
        "Enc": 1,
        "Availability": "Scarce",
        "Reach": "SB×3",
        "Damage": ["SB", 3],
        "Qualities": ["Impale"],
    },
    "Rock": {
        "Group": "Throwing",
        "Enc": 0,
        "Availability": "Common",
        "Reach": "SB×3",
        "Damage": ["SB"],
    },
    "Throwing Axe": {
        "Group": "Throwing",
        "Price": {"GC": 1},
        "Enc": 1,
        "Availability": "Common",
        "Reach": "SB×2",
        "Damage": ["SB", 3],
        "Qualities": ["Hack"],
    },
    "Throwing Knife": {
        "Group": "Throwing",
        "Price": {"SS": 18},
        "Enc": 0,
        "Availability": "Common",
        "Reach": "SB×2",
        "Damage": ["SB", 2],
    },
}

BLACKPOWDER_AMMO_DATA = {
    "Bullet and Powder (12)": {
        "Price": {"SS": 3, "BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Damage": [1],
        "Qualities": ["Impale", "Penetrating"],
    },
    "Improvised Shot and Powder": {
        "Price": {"BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Range": "Half weapon",
    },
    "Small Shot and Powder (12)": {
        "Price": {"SS": 3, "BP": 3},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Blast +1"],
    },
}

BOW_AMMO_DATA = {
    "Arrow (12)": {
        "Price": {"SS": 5},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Impale"],
    },
    "Elf Arrow": {
        "Price": {"SS": 6},
        "Enc": 0,
        "Availability": "Exotic",
        "Range": "+50",
        "Damage": [1],
        "Qualities": ["Accurate", "Impale", "Penetrating"],
    },
}

CROSSBOW_AMMO_DATA = {
    "Bolt (12)": {
        "Price": {"SS": 5},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Impale"],
    },
}

SLING_AMMO_DATA = {
    "Lead Bullet (12)": {
        "Price": {"BP": 4},
        "Enc": 0,
        "Availability": "Common",
        "Range": "-10",
        "Damage": [1],
        "Qualities": ["Pummel"],
    },
    "Stone Bullet (12)": {
        "Price": {"BP": 2},
        "Enc": 0,
        "Availability": "Common",
        "Qualities": ["Pummel"],
    },
}

MELEE_WEAPONS_DATA = (
    BASIC_DATA
    | CAVALRY_DATA
    | FENCING_DATA
    | BRAWLING_DATA
    | FLAIL_DATA
    | PARRY_DATA
    | POLEARM_DATA
    | TWO_HANDED_DATA
)

RANGED_WEAPONS_DATA = (
    BLACKPOWDER_DATA
    | BOW_DATA
    | CROSSBOW_DATA
    | ENGINEERING_DATA
    | ENTANGLING_DATA
    | EXPLOSIVES_DATA
    | SLING_DATA
    | THROWING_DATA
)

AMMUNITION_DATA = (
    BLACKPOWDER_AMMO_DATA | BOW_AMMO_DATA | CROSSBOW_AMMO_DATA | SLING_AMMO_DATA
)

WEAPONS_DATA = MELEE_WEAPONS_DATA | RANGED_WEAPONS_DATA
