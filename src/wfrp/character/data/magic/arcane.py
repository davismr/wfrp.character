from wfrp.character.data.magic.arcane_winds_of_magic import ARCANE_WINDS_OF_MAGIC_DATA

ARCANE_MAGIC_DATA = {
    "Aethyric Armour": {
        "CN": 2,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds+",
        "description": (
            "You gain +1 Armour Point to all Hit Locations as you wrap yourself in a "
            "protective swathe of magic."
        ),
    },
    "Aethyric Arms": {
        "CN": 2,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds+",
        "description": (
            "You create a melee weapon with a Damage equal to your Willpower Bonus. "
            "This may take any form, and so use any Melee Skill you may possess. The "
            "weapon counts as Magical."
        ),
    },
    "Arrow Shield": {
        "CN": 3,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds+",
        "description": (
            "Any missiles containing organic matter, such as arrows with wooden "
            "shafts, are automatically destroyed if they pass within the Area of "
            "Effect, causing no damage to their target. Missiles comprising only "
            "inorganic matter, such as throwing knives or pistol shots, are unaffected."
        ),
    },
    "Blast": {
        "CN": 4,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Instant",
        "description": (
            "You channel magic into an explosive blast. This is a magic missile with "
            "Damage +3 that targets everyone in the Area of Effect."
        ),
    },
    "Bolt": {
        "CN": 4,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "You channel magic into a damaging bolt. Bolt is a magic missile with a "
            "Damage of +4."
        ),
    },
    "Breath": {
        "CN": 6,
        "range": "1 yard",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "You immediately make a Breath attack, as if you had spent 2 Advantage to "
            "activate the Breath Creature Trait (see page 338). Breath is a magic "
            "missile with a Damage equal to your Toughness Bonus. The GM decides which "
            "type of Breath attack best suits your Arcane Magic Talent."
        ),
    },
    "Bridge": {
        "CN": 4,
        "range": "Willpower yards",
        "target": "AoE (see description)",
        "duration": "Willpower Bonus Rounds+",
        "description": (
            "You create a bridge of magical energy, with a maximum length and breadth "
            "of your Willpower Bonus in yards. For every +2 SL you may increase length "
            "or breadth by your Willpower Bonus in yards."
        ),
    },
    "Chain Attack": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "You channel a twisting spur of rupturing magic into your target. This is "
            "a magic missile with a Damage of +4. If Chain Attack reduces a target to "
            "0 Wounds, it leaps to another target within the spell’s initial range, "
            "and within Willpower Bonus yards of the previous target, inflicting the "
            "same Damage again. It may leap a maximum number of times equal to your "
            "Willpower Bonus. For every +2 SL achieved, it may chain to an additional "
            "target."
        ),
    },
    "Corrosive Blood": {
        "CN": 4,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You infuse yourself with magic, lending your blood a fearsome potency. "
            "You gain the Corrosive Blood Creature Trait (see page 339)."
        ),
    },
    "Dark Vision": {
        "CN": 1,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You boost your Second Sight to assist your mundane senses. While the "
            "spell is active, gain the Dark Vision Creature Trait (see page 339)."
        ),
    },
    "Distracting": {
        "CN": 4,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wreathe yourself in magic, which swirls around you, distracting your "
            "foes. While the spell is active, gain the Distracting Creature Trait "
            "(see page 339)."
        ),
    },
    "Dome": {
        "CN": 7,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You create a dome of magical energy overhead, blocking incoming attacks. "
            "Anyone within the Area of Effect gains the Ward (6+) Creature Trait "
            "(see page 343) against magical or ranged attacks originating outside the "
            "dome. Those within may attack out of the dome as normal, and the dome "
            "does not impede movement."
        ),
    },
    "Drop": {
        "CN": 1,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "You channel magic into an object being held by an opponent. This could be "
            "a weapon, a rope, or someone’s hand. Unless a Challenging (+0) Dexterity "
            "Test is passed, the item is dropped. For every +2 SL you may impose an "
            "additional –10 on the Dexterity Test."
        ),
    },
    "Entangle": {
        "CN": 3,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Special",
        "description": (
            "Using magic, you entrap your target, wrapping them in whatever suits your "
            "Lore: vines, shadows, their own clothing… Your target gains one Entangled "
            "Condition with a Strength equal to your Intelligence. For every +2 SL, "
            "you may give the target +1 additional Entangled Condition. The spell "
            "lasts until all Entangled Conditions are removed."
        ),
    },
    "Fearsome": {
        "CN": 3,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Shrouding yourself in magic, you become fearsome and intimidating. Gain "
            "Fear 1. For every +3 SL, you may increase your Fear value by one."
        ),
    },
    "Flight": {
        "CN": 8,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds+",
        "description": (
            "You can fly, whether by sprouting wings, ascending on a pillar of magical "
            "light, or some other method. Gain the Flight (Agility) Creature Trait "
            "(see page 339)."
        ),
    },
    "Magic Shield": {
        "CN": 4,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You encase yourself in bands of protective magic. While the spell is "
            "active, add +Willpower Bonus SL to any dispel attempts you make."
        ),
    },
    "Move Object": {
        "CN": 4,
        "range": "WP yards",
        "target": 1,
        "duration": "1 Round",
        "description": (
            "Using magic, you grab hold of an non-sentient object no larger than you, "
            "moving it with the sheer force of your will, which is considered to have "
            "a Strength equal to your Willpower. You may move the object up to "
            "Willpower Bonus yards. If anyone attempts to impede the object’s "
            "movement, make a Contested Willpower/Strength Test. For every +2 SL you "
            "may increase the distance the object is moved by Willpower Bonus yards."
        ),
    },
    "Mundane Aura": {
        "CN": 4,
        "range": "You",
        "target": "You",
        "duration": "Willpower minutes",
        "description": (
            "You drain all the Winds of Magic from within your body and your "
            "possessions, removing any magical aura. For the duration of the spell you "
            "appear mundane to the Magical Sense Talent and similar. You effectively "
            "have no magical ability and your magical nature cannot be detected by any "
            "means. While this spell is in effect, you cannot cast any other spells. "
            "Mundane Aura is immediately dispelled if you make a Channelling Test."
        ),
    },
    "Push": {
        "CN": 6,
        "range": "You",
        "target": "You",
        "duration": "Instant",
        "description": (
            "All living creatures within Willpower Bonus yards are pushed back your "
            "Willpower Bonus in yards and gain the Prone Condition. If this brings "
            "them into contact with a wall or other large obstacle, they take Damage "
            "equal to the distance travelled in yards. For every +2 SL, you may push "
            "creatures back another Willpower Bonus in yards."
        ),
    },
    "Teleport": {
        "CN": 5,
        "range": "You",
        "target": "You",
        "duration": "Instant",
        "description": (
            "Using magic, you can teleport up to your Willpower Bonus in yards. This "
            "movement allows you to traverse gaps, avoid perils and pitfalls, and "
            "ignore obstacles. For every +2 SL you may increase the distance travelled "
            "by your Willpower Bonus in yards."
        ),
    },
    "Terrifying": {
        "CN": 7,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": "You gain the Terror (1) Creature Trait (see page 191).",
    },
    "Ward": {
        "CN": 5,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wrap yourself in protective magic, gaining the Ward (9+) Creature "
            "Trait (see page 343)."
        ),
    },
}

ALL_ARCANE_MAGIC_DATA = dict(
    sorted((ARCANE_MAGIC_DATA | ARCANE_WINDS_OF_MAGIC_DATA).items())
)
