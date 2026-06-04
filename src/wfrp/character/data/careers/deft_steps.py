from copy import deepcopy

from wfrp.character.data.careers.academics import ACADEMIC_CLASS_DATA
from wfrp.character.data.careers.rogues import ROGUES_CLASS_DATA

DEFT_STEPS_CAREERS = {
    "Priest": [
        "Thief-Priest",
        "Gambler-Priest",
        "Trickster-Priest",
        "Liberator-Priest",
        "Dealer-Priest",
    ],
    "Thief": ["Pickpocket", "Burglar", "Embezzler"],
    "Charlatan": "Forger",
    "Messenger": "Muleskinner",
    "Hunter": "Poacher",
    "Warden": "Gamekeeper",
}

DEFT_STEPS_CLASS_DATA = {
    "Pickpocket": {
        "Prowler": deepcopy(ROGUES_CLASS_DATA["Thief"]["Prowler"]),
        "Pickpocket": deepcopy(ROGUES_CLASS_DATA["Thief"]["Thief"]),
        "Master Pickpocket": deepcopy(ROGUES_CLASS_DATA["Thief"]["Master Thief"]),
        "Cat Burglar": deepcopy(ROGUES_CLASS_DATA["Thief"]["Cat Burglar"]),
    },
    "Burglar": {
        "Prowler": deepcopy(ROGUES_CLASS_DATA["Thief"]["Prowler"]),
        "Burglar": deepcopy(ROGUES_CLASS_DATA["Thief"]["Thief"]),
        "Master Burglar": deepcopy(ROGUES_CLASS_DATA["Thief"]["Master Thief"]),
        "Cat Burglar": deepcopy(ROGUES_CLASS_DATA["Thief"]["Cat Burglar"]),
    },
    "Embezzler": {
        "Prowler": deepcopy(ROGUES_CLASS_DATA["Thief"]["Prowler"]),
        "Embezzler": deepcopy(ROGUES_CLASS_DATA["Thief"]["Thief"]),
        "Master Embezzler": deepcopy(ROGUES_CLASS_DATA["Thief"]["Master Thief"]),
        "Cat Burglar": deepcopy(ROGUES_CLASS_DATA["Thief"]["Cat Burglar"]),
    },
    "Thief-Priest": {
        "Initiate": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Initiative", "Agility", "Dexterity"],
            "skills": [
                "Athletics",
                "Climb",
                "Dodge",
                "Intuition",
                "Lore (Ranald)",
                "Perception",
                "Pick Lock",
                "Pray",
                "Sleight of Hand",
                "Stealth (Urban)",
            ],
            "talents": [
                "Bless (Ranald)",
                "Flee!",
                "Read/Write",
                "Suave",
            ],
            "trappings": [
                "Discreet Symbol of Ranald",
                "Leather Jerkin",
                "Sack",
            ],
        },
        "Thief-Priest": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": ["Fellowship"],
            "skills": [
                "Charm",
                "Endurance",
                "Entertain (Storytelling)",
                "Language (Thieves Tongue)",
                "Lore (Local)",
                "Secret Signs (Thief)",
            ],
            "talents": [
                "Etiquette (Ranaldans)",
                "Invoke (The Night Prowler)",
                "Luck",
                "Secret Identity",
            ],
            "trappings": [
                "Book (Ranald)",
                "Rope",
                "Trade Tools (Thief)",
            ],
        },
        "High Priest": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Intelligence"],
            "skills": [
                "Bribery",
                "Cool",
                "Evaluate",
                "Gossip",
            ],
            "talents": [
                "Alley Cat",
                "Etiquette (Criminals)",
                "Nimble Fingered",
                "Nose for Trouble",
            ],
            "trappings": [
                "Initiate Apprentice/Lookout",
                "Quality Dark Clothing",
                "Shrine of the Night Prowler",
            ],
        },
        "Shadow Prowler": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": ["Willpower"],
            "skills": [
                "Intimidate",
                "Leadership",
            ],
            "talents": [
                "Criminal",
                "Night Vision",
                "Pure Soul",
                "Shadow",
            ],
            "trappings": [
                "Mask",
                "Subordinate Thief-Priests",
            ],
        },
    },
    "Gambler-Priest": {
        "Initiate": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Initiative", "Dexterity", "Fellowship"],
            "skills": [
                "Charm",
                "Consume Alcohol",
                "Cool",
                "Gamble",
                "Gossip",
                "Intuition",
                "Lore (Ranald)",
                "Perception",
                "Pray",
                "Sleight of Hand",
            ],
            "talents": [
                "Bless (Ranald)",
                "Luck",
                "Holy Visions",
                "Suave",
            ],
            "trappings": [
                "Discreet Symbol of Ranald",
                "Deck of Cards",
                "Dice",
            ],
        },
        "Gambler-Priest": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Willpower"],
            "skills": [
                "Dodge",
                "Entertain (Storytelling)",
                "Evaluate",
                "Haggle",
                "Intimidate",
                "Melee (Basic)",
            ],
            "talents": [
                "Cardsharp",
                "Diceman",
                "Etiquette (Ranaldans)",
                "Invoke (The Gamester)",
            ],
            "trappings": [
                "Hand Weapon",
                "Lucky Charm",
                "Quality Clothing",
            ],
        },
        "High Priest": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": ["Intelligence"],
            "skills": [
                "Bribery",
                "Language (Any)",
                "Lore (Any)",
                "Research",
            ],
            "talents": [
                "Acute Sense (Any)",
                "Fast Hands",
                "Read/Write",
                "Super Numerate",
            ],
            "trappings": [
                "Initiate Apprentice",
                "Shrine of Ranald (Fixed or Portable)",
            ],
        },
        "Master of Chance": {
            "status": {"tier": "Silver", "standing": 5},
            "attributes": ["Agility"],
            "skills": [
                "Leadership",
                "Perform (Card Tricks)",
            ],
            "talents": [
                "Nose for Trouble",
                "Savvy",
                "Schemer",
                "Secret Identity",
            ],
            "trappings": [
                "Best Quality Clothes",
                "Subordinate Priests",
            ],
        },
    },
    "Trickster-Priest": {
        "Initiate": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Initiative", "Willpower", "Fellowship"],
            "skills": [
                "Bribery",
                "Charm",
                "Cool",
                "Intuition",
                "Entertain (Storytelling)",
                "Gossip",
                "Lore (Ranald)",
                "Perception",
                "Pray",
                "Sleight of Hand",
            ],
            "talents": [
                "Bless (Ranald)",
                "Cat-tongued",
                "Luck",
                "Suave",
            ],
            "trappings": [
                "Discreet Symbol of Ranald",
                "2 Sets of Clothing",
            ],
        },
        "Trickster-Priest": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Dexterity"],
            "skills": [
                "Athletics",
                "Entertain (Acting)",
                "Intimidate",
                "Language (Any)",
                "Melee (Basic)",
                "Stealth (Urban)",
            ],
            "talents": [
                "Etiquette (Ranaldans)",
                "Holy Visions",
                "Invoke (The Deceiver)",
                "Secret Identity",
            ],
            "trappings": [
                "Book (Ranald)",
                "Disguise Kit",
                "Hand Weapon",
            ],
        },
        "High Priest": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": ["Agility"],
            "skills": [
                "Art (Any)",
                "Dodge",
                "Perform (Acting)",
                "Secret Signs (Thief)",
            ],
            "talents": [
                "Blather",
                "Fast Hands",
                "Master of Disguise",
                "Mimic",
            ],
            "trappings": [
                "Cloak or Coat with Hidden Pockets",
                "Initiate Apprentice",
            ],
        },
        "Lord of Misrule": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": ["Intelligence"],
            "skills": [
                "Leadership",
                "Consume Alcohol",
            ],
            "talents": [
                "Nose for Trouble",
                "Public Speaker",
                "Pure Soul",
                "Savvy",
            ],
            "trappings": [
                "Subordinate Priests",
                "Trade Tools (Any)",
            ],
        },
    },
    "Liberator-Priest": {
        "Initiate": {
            "status": {"tier": "Brass", "standing": 1},
            "attributes": ["Agility", "Willpower", "Fellowship"],
            "skills": [
                "Bribery",
                "Charm",
                "Cool",
                "Entertain (Storytelling)",
                "Gossip",
                "Haggle",
                "Intuition",
                "Lore (Politics)",
                "Perception",
                "Pray",
            ],
            "talents": [
                "Argumentative",
                "Bless (Ranald)",
                "Holy Visions",
                "Luck",
            ],
            "trappings": [
                "Discreet Symbol of Ranald",
                "Leather Jack",
            ],
        },
        "Liberator-Priest": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": ["Intelligence"],
            "skills": [
                "Athletics",
                "Dodge",
                "Intimidate",
                "Lore (Local)",
                "Melee (Basic)",
                "Melee (Brawling)",
            ],
            "talents": [
                "Cat-tongued",
                "Etiquette (Ranaldans)",
                "Invoke (The Protector)",
                "Read/Write",
            ],
            "trappings": [
                "Hand Weapon",
                "Holy Book (Ranald)",
            ],
        },
        "High Priest": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Initiative"],
            "skills": [
                "Evaluate",
                "Heal",
                "Language (Thieves Tongue)",
                "Leadership",
            ],
            "talents": [
                "Impassioned Zeal",
                "Public Speaker",
                "Schemer",
                "Secret Identity",
            ],
            "trappings": [
                "Initiate Apprentice",
                "Shrine of Ranald",
                "Street Urchin Band",
            ],
        },
        "People’s Champion": {
            "status": {"tier": "Silver", "standing": 3},
            "attributes": ["Weapon Skill"],
            "skills": [
                "Language (Any)",
                "Stealth (Urban)",
            ],
            "talents": [
                "Disarm",
                "Gregarious",
                "Master Orator",
                "Pure Soul",
            ],
            "trappings": [
                "Grateful Local Common Folk",
                "Subordinate Priests",
            ],
        },
    },
    "Dealer-Priest": {
        "Initiate": deepcopy(ACADEMIC_CLASS_DATA["Priest"]["Initiate"]),
        "Dealer-Priest": deepcopy(ACADEMIC_CLASS_DATA["Priest"]["Priest"]),
        "High Priest": deepcopy(ACADEMIC_CLASS_DATA["Priest"]["High Priest"]),
        "Lector": deepcopy(ACADEMIC_CLASS_DATA["Priest"]["Lector"]),
    },
    "Forger": {
        "Fraudster": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Toughness", "Initiative", "Dexterity"],
            "skills": [
                "Art (Any One)",
                "Cool",
                "Consume Alcohol",
                "Gossip",
                "Haggle",
                "Intuition",
                "Perception",
                "Sleight of Hand",
                "Stealth (Urban)",
                "Trade (Artist or Smith)",
            ],
            "talents": [
                "Artistic",
                "Craftsman (Trade)",
                "Criminal",
                "Numismatics",
            ],
            "trappings": [
                "Coin Mould (any currency)",
                "Trade Tools",
            ],
        },
        "Forger": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Intelligence"],
            "skills": [
                "Art (Any One)",
                "Bribery",
                "Charm",
                "Evaluate",
                "Gamble",
                "Secret Signs (Thief)",
            ],
            "talents": [
                "Briber",
                "Nimble Fingered",
                "Read/Write",
                "Tinker",
            ],
            "trappings": [
                "Calligrapher’s Tools",
            ],
        },
        "Counterfeiter": {
            "status": {"tier": "Silver", "standing": 4},
            "attributes": ["Willpower"],
            "skills": [
                "Lore (Art)",
                "Lore (Heraldry)",
                "Research",
                "Trade (Any One)",
            ],
            "talents": [
                "Acute Sense (Any)",
                "Dealmaker",
                "Savvy",
                "Super Numerate",
            ],
            "trappings": [
                "Artist’s Tools",
                "Charlatan Contact",
                "Workshop",
            ],
        },
        "Master Counterfeiter": {
            "status": {"tier": "Gold", "standing": 2},
            "attributes": ["Fellowship"],
            "skills": [
                "Leadership",
                "Lore (History)",
            ],
            "talents": [
                "Kingpin",
                "Magnum Opus",
                "Master Tradesman (Any)",
                "Schemer",
            ],
            "trappings": [
                "2 Charlatan Subordinates",
                "Forged Guild Licence",
                "Quality Clothing",
            ],
        },
    },
    "Ranger-Priest of Taal": {
        "Initiate": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Toughness", "Agility", "Willpower"],
            "skills": [
                "Athletics",
                "Charm Animal",
                "Cool",
                "Endurance",
                "Intuition",
                "Lore (Theology)",
                "Outdoor Survival",
                "Perception",
                "Pray",
                "Ranged (Bow)",
            ],
            "talents": [
                "Bless (Taal)",
                "Holy Visions",
                "Orientation",
                "Rover",
            ],
            "trappings": [
                "Bow and 10 Arrows",
                "Cloak",
                "Religious Symbol (Taal)",
                "Sturdy Boots",
            ],
        },
        "Ranger-Priest": {
            "status": {"tier": "Brass", "standing": 5},
            "attributes": ["Fellowship"],
            "skills": [
                "Heal",
                "Intimidate",
                "Melee (Basic)",
                "Navigation",
                "Stealth (Rural)",
                "Track",
            ],
            "talents": [
                "Etiquette (Taal)",
                "Hunter’s Eye",
                "Invoke (Taal)",
                "Strider (Any)",
            ],
            "trappings": [
                "Backpack",
                "Bedroll",
                "Hand Weapon",
            ],
        },
        "High Priest": {
            "status": {"tier": "Silver", "standing": 4},
            "attributes": ["Initiative"],
            "skills": [
                "Animal Training (Any)",
                "Language (Any)",
                "Lore (Beasts)",
                "Ride (Horse)",
            ],
            "talents": [
                "Hardy",
                "Pure Soul",
                "Resistance (Any)",
                "Sure Shot",
            ],
            "trappings": [
                "Initiate Follower",
                "Religious Relic",
            ],
        },
        "Vice-hierarch": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": ["Intelligence"],
            "skills": [
                "Language (Any)",
                "Stealth (Urban)",
            ],
            "talents": [
                "Disarm",
                "Gregarious",
                "Master Orator",
                "Tenacious",
            ],
            "trappings": [
                "Animal Companion",
                "Subordinate Priests",
            ],
        },
    },
    "Muleskinner": {
        "Driver": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": ["Ballistic Skill", "Agility", "Willpower"],
            "skills": [
                "Animal Care",
                "Charm Animal",
                "Drive",
                "Endurance",
                "Gossip",
                "Lore (Local)",
                "Melee (Basic)",
                "Perception",
                "Ranged (Entangling)",
                "Ride (Horse)",
            ],
            "talents": [
                "Animal Affinity",
                "Crack the Whip",
                "Orientation",
                "Tenacious",
            ],
            "trappings": [
                "Gloves",
                "Leather Hat",
                "Travel Clothes",
                "Whip",
            ],
        },
        "Muleskinner": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": ["Intelligence"],
            "skills": [
                "Animal Training (Any)",
                "Dodge",
                "Language (Any)",
                "Navigation",
                "Outdoor Survival",
                "Ranged (Bow)",
            ],
            "talents": [
                "Coolheaded",
                "Seasoned Traveller",
                "Fearless (Any)",
                "Strider (Any)",
            ],
            "trappings": [
                "Tent",
                "Quality Hat",
            ],
        },
        "Caravan Guide": {
            "status": {"tier": "Silver", "standing": 4},
            "attributes": ["Initiative"],
            "skills": [
                "Cool",
                "Intuition",
                "Trade (Carpenter)",
                "Stealth (Rural)",
            ],
            "talents": [
                "Etiquette (Guilder)",
                "Nose for Trouble",
                "Stout-hearted",
                "Trick Riding",
            ],
            "trappings": [
                "Map",
                "Pack Animal",
                "Quality Travel Clothes",
                "Riding Horse and Tack",
            ],
        },
        "Caravan Master": {
            "status": {"tier": "Gold", "standing": 1},
            "attributes": ["Toughness"],
            "skills": [
                "Haggle",
                "Leadership",
            ],
            "talents": [
                "Dealmaker",
                "Inspiring",
                "Numismatics",
                "Read/Write",
            ],
            "trappings": [
                "Caravan",
                "Stable of Pack Animals",
            ],
        },
    },
    "Gamekeeper": {
        "Underkeeper": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": ["Ballistic Skill", "Initiative", "Intelligence"],
            "skills": [
                "Animal Care",
                "Climb",
                "Gossip",
                "Lore (Beasts)",
                "Melee (Basic)",
                "Outdoor Survival",
                "Perception",
                "Ranged (Bow)",
                "Set Trap",
                "Stealth (Rural)",
            ],
            "talents": [
                "Marksman",
                "Rover",
                "Strider (Any)",
                "Trapper",
            ],
            "trappings": [
                "Hat",
                "Bow and Arrow (12)",
                "Hand Weapon",
            ],
        },
        "Gamekeeper": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Weapon Skill"],
            "skills": [
                "Athletics",
                "Cool",
                "Endurance",
                "Intuition",
                "Lore (Local)",
                "Track",
            ],
            "talents": [
                "Hunter’s Eye",
                "Menacing",
                "Sharpshooter",
                "Strike to Stun",
            ],
            "trappings": [
                "Quality Hat",
                "Hunting Suit",
            ],
        },
        "Head Gamekeeper": {
            "status": {"tier": "Silver", "standing": 2},
            "attributes": ["Agility"],
            "skills": [
                "Animal Training (Any)",
                "Navigation",
                "Ranged (Blackpowder)",
                "Ride (Horse)",
            ],
            "talents": [
                "Accurate Shot",
                "Acute Sense (Any)",
                "Orientation",
                "Fast Shot",
            ],
            "trappings": [
                "Blackpowder Weapon",
                "Riding Horse with Saddle and Tack",
            ],
        },
        "Master Gamekeeper": {
            "status": {"tier": "Silver", "standing": 4},
            "attributes": ["Willpower"],
            "skills": [
                "Leadership",
                "Lore (Law)",
            ],
            "talents": [
                "Dealmaker",
                "Commanding Presence",
                "Etiquette (Servants)",
                "Read/Write",
            ],
            "trappings": [
                "Estate Cottage",
                "Quality Clothing",
            ],
        },
    },
    "Poacher": {
        "Scrumper": {
            "status": {"tier": "Brass", "standing": 2},
            "attributes": ["Ballistic Skill", "Agility", "Dexterity"],
            "skills": [
                "Bribery",
                "Climb",
                "Dodge",
                "Haggle",
                "Lore (Beasts)",
                "Outdoor Survival",
                "Perception",
                "Ranged (Sling)",
                "Set Trap",
                "Stealth (Rural)",
            ],
            "talents": [
                "Fisherman",
                "Flee!",
                "Strider (Any)",
                "Trapper",
            ],
            "trappings": [
                "Cloak",
                "Rod and Line",
                "Selection of Animal Traps",
                "Sling with 10 Stone Bullets",
            ],
        },
        "Poacher": {
            "status": {"tier": "Brass", "standing": 4},
            "attributes": ["Intelligence"],
            "skills": [
                "Athletics",
                "Cool",
                "Endurance",
                "Melee (Basic)",
                "Ranged (Bow)",
                "Track",
            ],
            "talents": [
                "Hunter’s Eye",
                "Marksman",
                "Rover",
                "Sharpshooter",
            ],
            "trappings": [
                "Bed Roll",
                "Bow and Arrow",
                "Tent",
            ],
        },
        "Master Poacher": {
            "status": {"tier": "Silver", "standing": 1},
            "attributes": ["Weapon Skill"],
            "skills": [
                "Animal Care",
                "Animal Training (Any)",
                "Navigation",
                "Ride (Horse)",
            ],
            "talents": [
                "Accurate Shot",
                "Acute Sense (Any)",
                "Criminal",
                "Fast Shot",
            ],
            "trappings": [
                "Hunting Hound or Hawk",
                "Quality Weapon",
            ],
        },
        "Champion Poacher": {
            "status": {"tier": "Silver", "standing": 4},
            "attributes": ["Initiative"],
            "skills": [
                "Intimidate",
                "Lore (Law)",
            ],
            "talents": [
                "Briber",
                "Dealmaker",
                "Kingpin",
                "Menacing",
            ],
            "trappings": [
                "Riding Horse with Saddle and Tack",
            ],
        },
    },
}

DEFT_STEPS_CLASS_DATA["Pickpocket"]["Prowler"]["skills"].append("Perform (Clowning)")
DEFT_STEPS_CLASS_DATA["Pickpocket"]["Prowler"]["skills"].append("Sleight of Hand")
DEFT_STEPS_CLASS_DATA["Pickpocket"]["Prowler"]["talents"].remove("Strike to Stun")
DEFT_STEPS_CLASS_DATA["Pickpocket"]["Prowler"]["talents"].append("Fast Hands")
DEFT_STEPS_CLASS_DATA["Burglar"]["Prowler"]["skills"].append("Lore (Local)")
DEFT_STEPS_CLASS_DATA["Burglar"]["Prowler"]["skills"].append("Melee (Brawling)")
DEFT_STEPS_CLASS_DATA["Burglar"]["Master Burglar"]["talents"].remove("Trapper")
DEFT_STEPS_CLASS_DATA["Burglar"]["Master Burglar"]["talents"].append("Secret Identity")
DEFT_STEPS_CLASS_DATA["Embezzler"]["Prowler"]["attributes"].remove("Agility")
DEFT_STEPS_CLASS_DATA["Embezzler"]["Prowler"]["attributes"].append("Intelligence")
DEFT_STEPS_CLASS_DATA["Embezzler"]["Prowler"]["skills"] = [
    "Bribery",
    "Charm",
    "Cool",
    "Dodge",
    "Endurance",
    "Evaluate",
    "Gossip",
    "Haggle",
    "Intuition",
    "Perception",
]
DEFT_STEPS_CLASS_DATA["Embezzler"]["Prowler"]["talents"] = [
    "Briber",
    "Embezzle",
    "Flee!",
    "Read/Write",
]
DEFT_STEPS_CLASS_DATA["Embezzler"]["Embezzler"]["talents"] = [
    "Blather",
    "Etiquette (Guilder)",
    "Fast Hands",
    "Numismatics",
]
DEFT_STEPS_CLASS_DATA["Embezzler"]["Master Embezzler"]["talents"] = [
    "Dealmaker",
    "Nimble Fingered",
    "Savvy",
    "Super Numerate",
]
DEFT_STEPS_CLASS_DATA["Embezzler"]["Cat Burglar"]["talents"] = [
    "Cat-tongued",
    "Luck",
    "Schemer",
    "Wealthy",
]
# XXX At Level 1 (Prowler) they make the following change to their
# available Trappings: The Character may replace their Prowler
# Trappings with a Writing Kit and Abacus.
DEFT_STEPS_CLASS_DATA["Embezzler"]["Prowler"]["trappings"]

DEFT_STEPS_CLASS_DATA["Dealer-Priest"]["Initiate"]["skills"].append("Haggle")
DEFT_STEPS_CLASS_DATA["Dealer-Priest"]["Initiate"]["skills"].append("Evaluate")
