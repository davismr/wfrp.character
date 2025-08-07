BASIC_SKILL_DATA = {
    "Art": {
        "characteristic": ("dexterity", "Dex"),
        "specialisations": [
            "Cartography",
            "Engraving",
            "Mosaics",
            "Painting",
            "Sculpture",
            "Tattoo",
            "Weaving",
        ],
    },
    "Athletics": {
        "characteristic": ("agility", "Ag"),
        "description": (
            "Your ability to run, jump and move with speed or grace, and to perform "
            "any general physical activity. Refer to Moving (see page 164) for details "
            "on using Athletics in combat movement."
        ),
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
    "Entertain": {
        "characteristic": ("fellowship", "Fel"),
        "specialisations": ["Acting", "Comedy", "Singing", "Storytelling"],
    },
    "Gamble": {"characteristic": ("intelligence", "Int")},
    "Gossip": {"characteristic": ("fellowship", "Fel")},
    "Haggle": {"characteristic": ("fellowship", "Fel")},
    "Intimidate": {"characteristic": ("strength", "S")},
    "Intuition": {"characteristic": ("initiative", "I")},
    "Leadership": {"characteristic": ("fellowship", "Fel")},
    "Melee": {
        "characteristic": ("weapon_skill", "WS"),
        "specialisations": [
            "Basic",
            "Brawling",
            "Cavalry",
            "Fencing",
            "Flail",
            "Parry",
            "Pole-Arm",
            "Two-Handed",
        ],
    },
    "Navigation": {"characteristic": ("initiative", "I")},
    "Outdoor Survival": {"characteristic": ("intelligence", "Int")},
    "Perception": {"characteristic": ("initiative", "I")},
    "Ride": {
        "characteristic": ("agility", "Ag"),
        "specialisations": ["Demigryph", "Great Wolf", "Griffon", "Horse", "Pegasus"],
    },
    "Row": {"characteristic": ("strength", "S")},
    "Stealth": {
        "characteristic": ("agility", "Ag"),
        "specialisations": ["Rural", "Underground", "Urban"],
    },
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
        "specialisations": [
            "Aqshy",
            "Azyr",
            "Chamon",
            "Dhar",
            "Ghur",
            "Ghyran",
            "Hysh",
            "Shyish",
            "Ulgu",
        ],
    },
    "Evaluate": {"characteristic": ("intelligence", "Int")},
    "Heal": {"characteristic": ("intelligence", "Int")},
    "Language": {
        "characteristic": ("intelligence", "Int"),
        # FIXME other languages?
        "specialisations": [
            "Battle Tongue",
            "Bretonnian",
            "Classical",
            "Guilder",
            "Khazalid",
            "Magick",
            "Thief",
            "Tilean",
        ],
    },
    "Lore": {
        "characteristic": ("intelligence", "Int"),
        "specialisations": [
            "Engineering",
            "Geology",
            "Heraldry",
            "History",
            "Law",
            "Magick",
            "Metallurgy",
            "Science",
            "Theology",
        ],
    },
    "Perform": {
        "characteristic": ("agility", "Ag"),
        "specialisations": [
            "Acrobatics",
            "Clowning",
            "Dancing",
            "Firebreathing",
            "Juggling",
            "Miming",
            "Rope Walking",
        ],
    },
    "Pick Lock": {"characteristic": ("dexterity", "Dex")},
    "Play": {
        "characteristic": ("dexterity", "Dex"),
        "specialisations": ["Bagpipe", "Lute", "Harpsichord", "Horn", "Violin"],
    },
    "Pray": {"characteristic": ("fellowship", "Fel")},
    "Ranged": {
        "characteristic": ("ballistic_skill", "BS"),
        "specialisations": [
            "Blackpowder",
            "Bow",
            "Crossbow",
            "Engineering",
            "Entangling",
            "Explosives",
            "Sling",
            "Throwing",
        ],
    },
    "Research": {"characteristic": ("intelligence", "Int")},
    "Sail": {"characteristic": ("agility", "Ag")},
    "Secret Signs": {
        "characteristic": ("intelligence", "Int"),
        # FIXME sub-specialisation
        "specialisations": [
            "Grey Order",
            "Guild (any one)",
            "Ranger",
            "Scout",
            "Thief",
            "Vagabond",
        ],
    },
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


SKILL_DATA = BASIC_SKILL_DATA | ADVANCED_SKILL_DATA
