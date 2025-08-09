from wfrp.character.utils import roll_2d10

RANGERS_CLASS_DATA = {
    "Bounty Hunter": {
        "Thief-taker": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Weapon Skill", "Toughness", "Agility"],
            "skills": [
                "Bribery",
                "Charm",
                "Gossip",
                "Haggle",
                "Intuition",
                "Melee (Basic)",
                "Outdoor Survival",
                "Perception",
            ],
            "talents": [
                "Break and Enter",
                "Shadow",
                "Strike to Stun",
                "Suave",
            ],
            "trappings": [
                "Hand Weapon",
                "Leather Jerkin",
                "Rope",
            ],
        },
    },
    "Coachman": {
        "Postilion": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Ballistic Skill", "Toughness", "Willpower"],
            "skills": [
                "Animal Care",
                "Charm Animal",
                "Climb",
                "Drive",
                "Endurance",
                "Perception",
                "Ranged (Entangling)",
                "Ride (Horse)",
            ],
            "talents": [
                "Animal Affinity",
                "Seasoned Traveller",
                "Trick Riding",
                "Tenacious",
            ],
            "trappings": [
                "Warm Coat and Gloves",
                "Whip",
            ],
        },
    },
    "Entertainer": {
        "Busker": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Agility", "Dexterity", "Fellowship"],
            "skills": [
                "Athletics",
                "Charm",
                "Entertain (Any)",
                "Gossip",
                "Haggle",
                "Perform (Any)",
                "Play (Any)",
                "Sleight of Hand",
            ],
            "talents": [
                "Attractive",
                "Mimic",
                "Public Speaker",
                "Suave",
            ],
            "trappings": [
                "Bowl",
                "Instrument",
            ],
        },
    },
    "Flagellant": {
        "Zealot": {
            "status": {"tier": "Brass", "standing": 0},
            "attributes": ["Weapon Skill", "Strength", "Toughness"],
            "skills": [
                "Dodge",
                "Endurance",
                "Heal",
                "Intimidate",
                "Intuition",
                "Lore (Sigmar)",
                "Melee (Flail)",
                "Outdoor Survival",
            ],
            "talents": [
                "Berserk Charge",
                "Frenzy",
                "Read/Write",
                "Stone Soup",
            ],
            "trappings": [
                "Flail",
                "Tattered Robes",
            ],
        },
    },
    "Messenger": {
        "Runner": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Toughness", "Initiative", "Agility"],
            "skills": [
                "Athletics",
                "Climb",
                "Dodge",
                "Endurance",
                "Gossip",
                "Navigation",
                "Perception",
                "Melee (Brawling)",
            ],
            "talents": [
                "Flee!",
                "Fleet Footed",
                "Sprinter",
                "Step Aside",
            ],
            "trappings": [
                "Scroll Case",
            ],
        },
    },
    "Pedlar": {
        "Vagabond": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Toughness", "Dexterity", "Willpower"],
            "skills": [
                "Charm",
                "Endurance",
                "Entertain (Storytelling)",
                "Gossip",
                "Haggle",
                "Intuition",
                "Outdoor Survival",
                "Stealth (Rural or Urban)",
            ],
            "talents": [
                "Fisherman",
                "Flee!",
                "Rover",
                "Tinker",
            ],
            "trappings": [
                "Backpack",
                "Bedroll",
                f"Goods worth {roll_2d10()} Brass",
                "Tent",
            ],
        },
    },
    "Road Warden": {
        "Toll Keeper": {
            "status": {"tier": "Brass", "standing": 5},
            "attributes": ["Ballistic Skill", "Toughness", "Initiative"],
            "skills": [
                "Bribery",
                "Consume Alcohol",
                "Gamble",
                "Gossip",
                "Haggle",
                "Melee (Basic)",
                "Perception",
                "Ranged (Crossbow)",
            ],
            "talents": [
                "Coolheaded",
                "Embezzle",
                "Marksman",
                "Numismatics",
            ],
            "trappings": [
                "Crossbow with 10 Bolts",
                "Leather Jack",
            ],
        },
    },
    "Witch Hunter": {
        "Interrogator": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Weapon Skill", "Toughness", "Willpower"],
            "skills": [
                "Charm",
                "Consume Alcohol",
                "Heal",
                "Intimidate",
                "Intuition",
                "Lore (Torture)",
                "Melee (Brawling)",
                "Perception",
            ],
            "talents": [
                "Coolheaded",
                "Menacing",
                "Read/Write",
                "Resolute",
            ],
            "trappings": [
                "Hand Weapon",
                "Instruments of Torture",
            ],
        },
    },
}
