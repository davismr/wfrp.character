BLESSINGS_DATA = {
    "Blessing of Battle": {
        "description": "Your target gains +10 WS.",
    },
    "Blessing of Breath": {
        "description": (
            "Your target does not need to breathe and ignores rules for suffocation."
        ),
    },
    "Blessing of Charisma": {
        "description": "Your target gains +10 Fellowship.",
    },
    "Blessing of Conscience": {
        "description": (
            "Your target must pass a Average (+20) Willpower Test to break any of the "
            "Strictures of your deity. If they fail, they are overcome with Shame and "
            "do not take the action."
        ),
    },
    "Blessing of Courage": {
        "description": "Your target gains +10 Willpower.",
    },
    "Blessing of Finesse": {
        "description": "Your target gains +10 Dexterity.",
    },
    "Blessing of Fortune": {
        "description": (
            "Your target’s next failed test may be rerolled. The reroll must stand."
        ),
    },
    "Blessing of Grace": {
        "description": "Your target gains +10 Agility.",
    },
    "Blessing of Hardiness": {
        "description": "Your target gains +10 Toughness.",
    },
    "Blessing of Healing": {
        "description": "Your target heals +1 Wound.",
    },
    "Blessing of The Hunt": {
        "description": "Your target gains +10 Ballistic Skill.",
    },
    "Blessing of Might": {
        "description": "Your target gains +10 Strength.",
    },
    "Blessing of Protection": {
        "description": (
            "Enemies must make a Average (+20) Willpower Test to attack your target as "
            "shame wells within for considering violence. If they fail, they must "
            "choose a different target, or a different Action."
        ),
    },
    "Blessing of Recuperation": {
        "description": (
            "Your target may reduce the duration of 1 disease with which they are "
            "afflicted by 1 day. This prayer may only be attempted once per instance "
            "of a disease per person."
        ),
    },
    "Blessing of Righteousness": {
        "description": "Your target’s weapon counts as Magical.",
    },
    "Blessing of Savagery": {
        "description": (
            "When your target next inflicts a Critical Wound, roll twice and choose "
            "the best result."
        ),
    },
    "Blessing of Tenacity": {
        "description": "Your target may remove 1 condition.",
    },
    "Blessing of Wisdom": {
        "description": "Your target gains +10 Intelligence.",
    },
    "Blessing of Wit": {
        "description": "Your target gains +10 Initiative.",
    },
}

for blessing in BLESSINGS_DATA:
    BLESSINGS_DATA[blessing]["target"] = 1
    BLESSINGS_DATA[blessing]["CN"] = None
    if blessing in ["Blessing of Healing", "Blessing of Recuperation"]:
        BLESSINGS_DATA[blessing]["range"] = "touch"
        BLESSINGS_DATA[blessing]["duration"] = "Instant"
    else:
        BLESSINGS_DATA[blessing]["range"] = "6 yards"
        BLESSINGS_DATA[blessing]["duration"] = "6 rounds"


def get_blessings(divine_lore):  # noqa: C901
    blessings = {}
    if divine_lore in ["Manann", "Stromfels"]:
        blessings["Blessing of Battle"] = BLESSINGS_DATA["Blessing of Battle"]
        blessings["Blessing of Breath"] = BLESSINGS_DATA["Blessing of Breath"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Hardiness"] = BLESSINGS_DATA["Blessing of Hardiness"]
        blessings["Blessing of Savagery"] = BLESSINGS_DATA["Blessing of Savagery"]
        blessings["Blessing of Tenacity"] = BLESSINGS_DATA["Blessing of Tenacity"]
    elif divine_lore == "Morr":
        blessings["Blessing of Breath"] = BLESSINGS_DATA["Blessing of Breath"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Fortune"] = BLESSINGS_DATA["Blessing of Fortune"]
        blessings["Blessing of Righteousness"] = BLESSINGS_DATA[
            "Blessing of Righteousness"
        ]
        blessings["Blessing of Tenacity"] = BLESSINGS_DATA["Blessing of Tenacity"]
        blessings["Blessing of Wisdom"] = BLESSINGS_DATA["Blessing of Wisdom"]
    elif divine_lore == "Myrmidia":
        blessings["Blessing of Battle"] = BLESSINGS_DATA["Blessing of Battle"]
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Fortune"] = BLESSINGS_DATA["Blessing of Fortune"]
        blessings["Blessing of Protection"] = BLESSINGS_DATA["Blessing of Protection"]
        blessings["Blessing of Righteousness"] = BLESSINGS_DATA[
            "Blessing of Righteousness"
        ]
    elif divine_lore == "Ranald":
        blessings["Blessing of Charisma"] = BLESSINGS_DATA["Blessing of Charisma"]
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Finesse"] = BLESSINGS_DATA["Blessing of Finesse"]
        blessings["Blessing of Fortune"] = BLESSINGS_DATA["Blessing of Fortune"]
        blessings["Blessing of Protection"] = BLESSINGS_DATA["Blessing of Protection"]
        blessings["Blessing of Wit"] = BLESSINGS_DATA["Blessing of Wit"]
    elif divine_lore == "Rhya":
        blessings["Blessing of Breath"] = BLESSINGS_DATA["Blessing of Breath"]
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Grace"] = BLESSINGS_DATA["Blessing of Grace"]
        blessings["Blessing of Healing"] = BLESSINGS_DATA["Blessing of Healing"]
        blessings["Blessing of Protection"] = BLESSINGS_DATA["Blessing of Protection"]
        blessings["Blessing of Recuperation"] = BLESSINGS_DATA[
            "Blessing of Recuperation"
        ]
    elif divine_lore == "Shallya":
        blessings["Blessing of Breath"] = BLESSINGS_DATA["Blessing of Breath"]
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Healing"] = BLESSINGS_DATA["Blessing of Healing"]
        blessings["Blessing of Protection"] = BLESSINGS_DATA["Blessing of Protection"]
        blessings["Blessing of Recuperation"] = BLESSINGS_DATA[
            "Blessing of Recuperation"
        ]
        blessings["Blessing of Tenacity"] = BLESSINGS_DATA["Blessing of Tenacity"]
    elif divine_lore == "Sigmar":
        blessings["Blessing of Battle"] = BLESSINGS_DATA["Blessing of Battle"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Hardiness"] = BLESSINGS_DATA["Blessing of Hardiness"]
        blessings["Blessing of Might"] = BLESSINGS_DATA["Blessing of Might"]
        blessings["Blessing of Protection"] = BLESSINGS_DATA["Blessing of Protection"]
        blessings["Blessing of Righteousness"] = BLESSINGS_DATA[
            "Blessing of Righteousness"
        ]
    elif divine_lore == "Taal":
        blessings["Blessing of Battle"] = BLESSINGS_DATA["Blessing of Battle"]
        blessings["Blessing of Breath"] = BLESSINGS_DATA["Blessing of Breath"]
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Hardiness"] = BLESSINGS_DATA["Blessing of Hardiness"]
        blessings["Blessing of The Hunt"] = BLESSINGS_DATA["Blessing of The Hunt"]
        blessings["Blessing of Savagery"] = BLESSINGS_DATA["Blessing of Savagery"]
    elif divine_lore == "Ulric":
        blessings["Blessing of Battle"] = BLESSINGS_DATA["Blessing of Battle"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Hardiness"] = BLESSINGS_DATA["Blessing of Hardiness"]
        blessings["Blessing of Might"] = BLESSINGS_DATA["Blessing of Might"]
        blessings["Blessing of Savagery"] = BLESSINGS_DATA["Blessing of Savagery"]
        blessings["Blessing of Tenacity"] = BLESSINGS_DATA["Blessing of Tenacity"]
    elif divine_lore == "Verena":
        blessings["Blessing of Conscience"] = BLESSINGS_DATA["Blessing of Conscience"]
        blessings["Blessing of Courage"] = BLESSINGS_DATA["Blessing of Courage"]
        blessings["Blessing of Fortune"] = BLESSINGS_DATA["Blessing of Fortune"]
        blessings["Blessing of Righteousness"] = BLESSINGS_DATA[
            "Blessing of Righteousness"
        ]
        blessings["Blessing of Wisdom"] = BLESSINGS_DATA["Blessing of Wisdom"]
        blessings["Blessing of Wit"] = BLESSINGS_DATA["Blessing of Wit"]
    else:
        raise NotImplementedError(
            f"Divine blessings for {divine_lore} is not available"
        )
    return blessings
