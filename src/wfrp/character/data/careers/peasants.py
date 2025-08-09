from wfrp.character.utils import roll_d10

PEASANTS_CLASS_DATA = {
    "Bailiff": {
        "Tax Collector": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Weapon Skill", "Initiative", "Willpower"],
            "skills": [
                "Cool",
                "Dodge",
                "Endurance",
                "Gossip",
                "Haggle",
                "Intimidate",
                "Melee (Basic)",
                "Perception",
            ],
            "talents": [
                "Embezzle",
                "Numismatics",
                "Strong Back",
                "Tenacious",
            ],
            "trappings": [
                "Hand weapon",
                "small lock box",
            ],
        },
    },
    "Hedge Witch": {
        "Hedge Apprentice": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Toughness", "Initiative", "Dexterity"],
            "skills": [
                "Channelling",
                "Endurance",
                "Intuition",
                "Language (Magick)",
                "Lore (Folklore)",
                "Lore (Herbs)",
                "Outdoor Survival",
                "Perception",
            ],
            "talents": [
                "Fast Hands",
                "Petty Magic",
                "Rover",
                "Strider (Woodlands)",
            ],
            "trappings": [
                f"{roll_d10()} Lucky Charms",
                "Quarterstaff",
                "Backpack",
            ],
        },
    },
    "Herbalist": {
        "Herb Gatherer": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Toughness", "Initiative", "Agility"],
            "skills": [
                "Charm Animal",
                "Climb",
                "Endurance",
                "Lore (Herbs)",
                "Outdoor Survival",
                "Perception",
                "Swim",
                "Trade (Herbalist)",
            ],
            "talents": [
                "Acute Sense (Taste)",
                "Orientation",
                "Rover",
                "Strider (any)",
            ],
            "trappings": [
                "Boots",
                "Cloak",
                "Sling Bag containing Assortment of Herbs",
            ],
        },
    },
    "Hunter": {
        "Trapper": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Strength", "Toughness", "Dexterity"],
            "skills": [
                "Charm Animal",
                "Climb",
                "Endurance",
                "Lore (Beasts)",
                "Outdoor Survival",
                "Perception",
                "Ranged (Sling)",
                "Set Trap",
            ],
            "talents": [
                "Hardy",
                "Rover",
                "Strider (any)",
                "Trapper",
            ],
            "trappings": [
                "Selection of Animal Traps",
                "Hand Weapon",
                "Sling with 10 Stone Bullets",
                "Sturdy Boots and Cloak",
            ],
        },
    },
    "Miner": {
        "Prospector": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Strength", "Toughness", "Dexterity"],
            "skills": [
                "Cool",
                "Endurance",
                "Intuition",
                "Lore (Local)",
                "Melee (Two-handed)",
                "Outdoor Survival",
                "Perception",
                "Swim",
            ],
            "talents": [
                "Rover",
                "Strider (Rocky)",
                "Sturdy",
                "Tenacious",
            ],
            "trappings": [
                "Charcoal Stick",
                "Crude Map",
                "Pan",
                "Spade",
            ],
        },
    },
    "Mystic": {
        "Fortune Teller": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Initiative", "Dexterity", "Fellowship"],
            "skills": [
                "Charm",
                "Entertain (Fortune Telling)",
                "Dodge",
                "Gossip",
                "Haggle",
                "Intuition",
                "Perception",
                "Sleight of Hand",
            ],
            "talents": [
                "Attractive",
                "Luck",
                "Second Sight",
                "Suave",
            ],
            "trappings": [
                "Deck of Cards or Dice",
                "Cheap Jewellery",
            ],
        },
    },
    "Scout": {
        "Guide": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Toughness", "Initiative", "Agility"],
            "skills": [
                "Charm Animal",
                "Climb",
                "Endurance",
                "Gossip",
                "Lore (Local)",
                "Melee (Basic)",
                "Outdoor Survival",
                "Perception",
            ],
            "talents": [
                "Orientation",
                "Rover",
                "Sharp",
                "Strider (any)",
            ],
            "trappings": [
                "Hand Weapon",
                "Leather Jack",
                "Sturdy Boots and Cloak",
                "Rope",
            ],
        },
    },
    "Villager": {
        "Peasant": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Strength", "Toughness", "Agility"],
            "skills": [
                "Animal Care",
                "Athletics",
                "Consume Alcohol",
                "Endurance",
                "Gossip",
                "Melee (Brawling)",
                "Lore (Local)",
                "Outdoor Survival",
            ],
            "talents": [
                "Rover",
                "Strong Back",
                "Strong-minded",
                "Stone Soup",
            ],
            "trappings": [],
        },
    },
}
