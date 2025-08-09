from wfrp.character.utils import roll_3d10

ROGUES_CLASS_DATA = {
    "Bawd": {
        "Hustler": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Agility", "Dexterity", "Fellowship"],
            "skills": [
                "Bribery",
                "Charm",
                "Consume Alcohol",
                "Entertain (Any)",
                "Gamble",
                "Gossip",
                "Haggle",
                "Intimidate",
            ],
            "talents": [
                "Attractive",
                "Alley Cat",
                "Blather",
                "Gregarious",
            ],
            "trappings": [
                "Flask of Spirits",
            ],
        },
    },
    "Charlatan": {
        "Swindler": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Initiative", "Dexterity", "Fellowship"],
            "skills": [
                "Bribery",
                "Consume Alcohol",
                "Charm",
                "Entertain (Storytelling)",
                "Gamble",
                "Gossip",
                "Haggle",
                "Sleight of Hand",
            ],
            "talents": [
                "Cardsharp",
                "Diceman",
                "Etiquette (Any)",
                "Luck",
            ],
            "trappings": [
                "Backpack",
                "2 Sets of Clothing",
                "Deck of Cards",
                "Dice",
            ],
        },
    },
    "Fence": {
        "Broker": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Initiative", "Agility", "Fellowship"],
            "skills": [
                "Charm",
                "Consume Alcohol",
                "Dodge",
                "Evaluate",
                "Gamble",
                "Gossip",
                "Haggle",
                "Melee (Basic)",
            ],
            "talents": [
                "Alley Cat",
                "Cardsharp",
                "Dealmaker",
                "Gregarious",
            ],
            "trappings": [
                "Hand Weapon",
                f"Stolen Goods worth {roll_3d10()} Shillings",
            ],
        },
    },
    "Grave Robber": {
        "Body Snatcher": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Strength", "Initiative", "Willpower"],
            "skills": [
                "Climb",
                "Cool",
                "Dodge",
                "Endurance",
                "Gossip",
                "Intuition",
                "Perception",
                "Stealth (Any)",
            ],
            "talents": [
                "Alley Cat",
                "Criminal",
                "Flee!",
                "Strong Back",
            ],
            "trappings": [
                "Crowbar",
                "Handcart",
                "Hooded Cloak",
                "Tarpaulin",
            ],
        },
    },
    "Outlaw": {
        "Brigand": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Weapon Skill", "Strength", "Toughness"],
            "skills": [
                "Athletics",
                "Consume Alcohol",
                "Cool",
                "Endurance",
                "Gamble",
                "Intimidate",
                "Melee (Basic)",
                "Outdoor Survival",
            ],
            "talents": [
                "Combat Aware",
                "Criminal",
                "Rover",
                "Flee!",
            ],
            "trappings": [
                "Bedroll",
                "Hand Weapon",
                "Leather Jerkin",
                "Tinderbox",
            ],
        },
    },
    "Racketeer": {
        "Thug": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Weapon Skill", "Strength", "Toughness"],
            "skills": [
                "Consume Alcohol",
                "Cool",
                "Dodge",
                "Endurance",
                "Intimidate",
                "Lore (Local)",
                "Melee (Brawling)",
                "Stealth (Urban)",
            ],
            "talents": [
                "Criminal",
                "Etiquette (Criminals)",
                "Menacing",
                "Strike Mighty Blow",
            ],
            "trappings": [
                "Knuckledusters",
                "Leather Jack",
            ],
        },
    },
    "Thief": {
        "Prowler": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Initiative", "Agility", "Willpower"],
            "skills": [
                "Athletics",
                "Climb",
                "Cool",
                "Dodge",
                "Endurance",
                "Intuition",
                "Perception",
                "Stealth (Urban)",
            ],
            "talents": [
                "Alley Cat",
                "Criminal",
                "Flee!",
                "Strike to Stun",
            ],
            "trappings": [
                "Crowbar",
                "Leather Jerkin",
                "Sack",
            ],
        },
    },
    "Witch": {
        "Hexer": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Weapon Skill", "Toughness", "Willpower"],
            "skills": [
                "Channelling",
                "Cool",
                "Endurance",
                "Gossip",
                "Intimidate",
                "Language (Magick)",
                "Sleight of Hand",
                "Stealth (Rural)",
            ],
            "talents": [
                "Criminal",
                "Instinctive Diction",
                "Menacing",
                "Petty Magic",
            ],
            "trappings": [
                "Candles",
                "Chalk",
                "Doll",
                "Pins",
            ],
        },
    },
}
