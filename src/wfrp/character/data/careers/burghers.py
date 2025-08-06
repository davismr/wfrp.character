from wfrp.character.utils import roll_3d10
from wfrp.character.utils import roll_d10

BURGHERS_CLASS_DATA = {
    "Agitator": {
        "class": "Burghers",
        "Pamphleteer": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Ballistic Skill", "Intelligence", "Fellowship"],
            "skills": [
                "Art (Writing)",
                "Bribery",
                "Charm",
                "Consume Alcohol",
                "Gossip",
                "Haggle",
                "Lore (Politics)",
                "Trade (Printing)",
            ],
            "talents": [
                "Blather",
                "Gregarious",
                "Panhandle",
                "Read/Write",
            ],
            "trappings": [
                "Writing Kit",
                "Hammer and Nails",
                "Pile of Leaflets",
            ],
        },
    },
    "Artisan": {
        "class": "Burghers",
        "Apprentice Artisan": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Strength", "Toughness", "Dexterity"],
            "skills": [
                "Athletics",
                "Cool",
                "Consume Alcohol",
                "Dodge",
                "Endurance",
                "Evaluate",
                "Stealth (Urban)",
                "Trade (Any)",
            ],
            "talents": [
                "Artistic",
                "Craftsman (Any)",
                "Strong Back",
                "Very Strong",
            ],
            "trappings": [
                "Chalk",
                "Leather Jerkin",
                f"{roll_d10()} rags",
            ],
        },
    },
    "Beggar": {
        "class": "Burghers",
        "Pauper": {
            "status": {"tier": "Brass", "standing": 0},
            "attributes": ["Toughness", "Agility", "Fellowship"],
            "skills": [
                "Athletics",
                "Charm",
                "Consume Alcohol",
                "Cool",
                "Dodge",
                "Endurance",
                "Intuition",
                "Stealth (Urban)",
            ],
            "talents": [
                "Panhandle",
                "Resistance (Disease)",
                "Stone Soup",
                "Very Resilient",
            ],
            "trappings": [
                "Poor Quality Blanket",
                "Cup",
            ],
        },
    },
    "Investigator": {
        "class": "Burghers",
        "Sleuth": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Initiative", "Agility", "Intelligence"],
            "skills": [
                "Charm",
                "Climb",
                "Cool",
                "Gossip",
                "Intuition",
                "Perception",
                "Stealth (Urban)",
                "Track",
            ],
            "talents": [
                "Alley Cat",
                "Beneath Notice",
                "Read/Write",
                "Sharp",
            ],
            "trappings": [
                "Lantern",
                "Lamp Oil,",
                "Journal",
                "Quill and Ink",
            ],
        },
    },
    "Merchant": {
        "class": "Burghers",
        "Trader": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": ["Agility", "Willpower", "Fellowship"],
            "skills": [
                "Animal Care",
                "Bribery",
                "Charm",
                "Consume Alcohol",
                "Drive",
                "Gamble",
                "Gossip",
                "Haggle",
            ],
            "talents": [
                "Blather",
                "Dealmaker",
                "Read/Write",
                "Suave",
            ],
            "trappings": [
                "Abacus",
                "Mule and Cart",
                "Canvas Tarpaulin",
                f"{roll_3d10()} Silver Shillings",
            ],
        },
    },
    "Rat Catcher": {
        "class": "Burghers",
        "Rat Hunter": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Weapon Skill", "Ballistic Skill", "Willpower"],
            "skills": [
                "Athletics",
                "Animal Training (Dog)",
                "Charm Animal",
                "Consume Alcohol",
                "Endurance",
                "Melee (Basic)",
                "Ranged (Sling)",
                "Stealth (Underground or Urban)",
            ],
            "talents": [
                "Night Vision",
                "Resistance (Disease)",
                "Strike Mighty Blow",
                "Strike to Stun",
            ],
            "trappings": [
                "Sling with Ammunition",
                "Sack",
                "Small but Vicious Dog",
            ],
        },
    },
    "Townsman": {
        "class": "Burghers",
        "Clerk": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Agility", "Intelligence", "Fellowship"],
            "skills": [
                "Charm",
                "Climb",
                "Consume Alcohol",
                "Drive",
                "Dodge",
                "Gamble",
                "Gossip",
                "Haggle",
            ],
            "talents": [
                "Alley Cat",
                "Beneath Notice",
                "Etiquette (Servants)",
                "Sturdy",
            ],
            "trappings": [
                "Lodgings",
                "Sturdy Boots",
            ],
        },
    },
    "Watchman": {
        "class": "Burghers",
        "Watch Recruit": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Weapon Skill", "Strength", "Fellowship"],
            "skills": [
                "Athletics",
                "Climb",
                "Consume Alcohol",
                "Dodge",
                "Endurance",
                "Gamble",
                "Melee (Any)",
                "Perception",
            ],
            "talents": [
                "Drilled",
                "Hardy",
                "Strike to Stun",
                "Tenacious",
            ],
            "trappings": [
                "Hand Weapon",
                "Leather Jack",
                "Uniform",
            ],
        },
    },
}
