from wfrp.character.utils import roll_3d10
from wfrp.character.utils import roll_d10

COURTIERS_CLASS_DATA = {
    "Advisor": {
        "Aide": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": ["Toughness", "Initiative", "Agility"],
            "skills": [
                "Bribery",
                "Consume Alcohol",
                "Endurance",
                "Gossip",
                "Haggle",
                "Language (Classical)",
                "Lore (Politics)",
                "Perception",
            ],
            "talents": [
                "Beneath Notice",
                "Etiquette (Any)",
                "Gregarious",
                "Read/Write",
            ],
            "trappings": [
                "Writing Kit",
            ],
        },
    },
    "Artist": {
        "Apprentice Artist": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Strength", "Initiative", "Dexterity"],
            "skills": [
                "Art (Any)",
                "Cool",
                "Consume Alcohol",
                "Evaluate",
                "Endurance",
                "Gossip",
                "Perception",
                "Stealth (Urban)",
            ],
            "talents": [
                "Artistic",
                "Sharp",
                "Strong Back",
                "Tenacious",
            ],
            "trappings": [
                "Brush or Chisel or Quill Pen",
            ],
        },
    },
    "Duellist": {
        "Fencer": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": ["Weapon Skill", "Initiative", "Dexterity"],
            "skills": [
                "Athletics",
                "Dodge",
                "Endurance",
                "Heal",
                "Intuition",
                "Language (Classical)",
                "Melee (Any)",
                "Perception",
            ],
            "talents": [
                "Beat Blade",
                "Distract",
                "Feint",
                "Step Aside",
            ],
            "trappings": [
                "Hand Weapon or Rapier",
                "Sling Bag containing Clothing",
                f"{roll_d10()} Bandages",
            ],
        },
    },
    "Envoy": {
        "Herald": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": ["Toughness", "Agility", "Fellowship"],
            "skills": [
                "Athletics",
                "Charm",
                "Drive",
                "Dodge",
                "Endurance",
                "Intuition",
                "Ride (Horse)",
                "Row",
            ],
            "talents": [
                "Blather",
                "Etiquette (Nobles)",
                "Read/Write",
                "Suave",
            ],
            "trappings": [
                "Leather Jack",
                "Livery",
                "Scroll Case",
            ],
        },
    },
    "Noble": {
        "Scion": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": ["Weapon Skill", "Initiative", "Dexterity"],
            "skills": [
                "Bribery",
                "Consume Alcohol",
                "Gamble",
                "Intimidate",
                "Leadership",
                "Lore (Heraldry)",
                "Melee (Fencing)",
                "Play (Any)",
            ],
            "talents": [
                "Etiquette (Nobles)",
                "Luck",
                "Noble Blood",
                "Read/Write",
            ],
            "trappings": [
                "Courtly Garb",
                "Foil or Hand Mirror",
                f"Jewellery worth {roll_3d10()} GC",
                "Personal Servant",
            ],
        },
    },
    "Servant": {
        "Menial": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Strength", "Toughness", "Agility"],
            "skills": [
                "Athletics",
                "Climb",
                "Drive",
                "Dodge",
                "Endurance",
                "Intuition",
                "Perception",
                "Stealth (Any)",
            ],
            "talents": [
                "Beneath Notice",
                "Strong Back",
                "Strong-minded",
                "Sturdy",
            ],
            "trappings": [
                "Floor Brush",
            ],
        },
    },
    "Spy": {
        "Informer": {
            "status": {"tier": "Brass", "standing": 3},
            "attributes": ["Agility", "Willpower", "Fellowship"],
            "skills": [
                "Bribery",
                "Charm",
                "Cool",
                "Gamble",
                "Gossip",
                "Haggle",
                "Perception",
                "Stealth (Any)",
            ],
            "talents": [
                "Blather",
                "Carouser",
                "Gregarious",
                "Shadow",
            ],
            "trappings": [
                "Charcoal stick",
                "Sling Bag containing 2 different sets of clothing and Hooded Cloak",
            ],
        },
    },
    "Warden": {
        "Custodian": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Strength", "Toughness", "Willpower"],
            "skills": [
                "Athletics",
                "Charm Animal",
                "Consume Alcohol",
                "Cool",
                "Endurance",
                "Intuition",
                "Lore (Local)",
                "Perception",
            ],
            "talents": [
                "Menacing",
                "Night Vision",
                "Sharp",
                "Strike to Stun",
            ],
            "trappings": [
                "Keys",
                "Lantern",
                "Lamp Oil",
                "Livery",
            ],
        },
    },
}
