LORE_BEASTS_DATA = {
    "Amber Talons": {
        "CN": 6,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Your nails grow into wickedly sharp talons of crystal amber. Unarmed "
            "attacks made using Melee (Brawling) count as magical, have a Damage equal "
            "to your Willpower Bonus, and inflict +1 Bleeding Condition whenever they "
            "cause a loss of Wounds."
        ),
    },
    "Beast Form": {
        "CN": 5,
        "range": "You",
        "target": "You",
        "duration": "Willpower minutes",
        "description": (
            "You infuse your very bones and flesh with Ghur, warping your body into "
            "that of a creature. When cast, select a new form from any of the Beasts "
            "of the Reikland section of the Bestiary. Gain all the standard Traits of "
            "the creature, except the Bestial Trait. Further, replace your S, T, Agi, "
            "and Dex with those of the creature, then recalculate your Wounds. For "
            "every + 2 SL, you may include 1 of the included Optional Creature Trait. "
            "While in Beast Form, you look like a normal version of the creature, with "
            "amber and brown colouring. You may not speak, which means you cannot cast "
            "spells, or attempt to dispel. If you have lost any Wounds when the spell "
            "ends, you lose the same number of Wounds when you revert to your true "
            "form, to a minimum of 0 Wounds."
        ),
    },
    "Beast Master": {
        "CN": 10,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Willpower Bonus days",
        "description": (
            "Your breath steams and your eyes take on a shining amber sheen as Ghur "
            "suffuses you. Your gaze and words convince 1 creature possessing the "
            "Bestial trait that you are its pack master, and it will fight to the "
            "death to protect you. While subject to your mastery it will follow your "
            "instructions, instinctively understanding simple instructions. If the "
            "creature is released from the spell — through the duration running out, "
            "or the spell being dispelled — it will retain enough residual respect and "
            "fear not to attack you, unless compelled to. Your allies may not be so "
            "fortunate."
        ),
    },
    "Beast Tongue": {
        "CN": 3,
        "range": "You",
        "target": "You",
        "duration": "Willpower minutes",
        "description": (
            "You can commune with all creatures possessing the Bestial Trait. Ghur "
            "clogs your throat, and your language comes out as snarls, hisses, and "
            "roars as befits the beasts to whom you talk. While the creatures are not "
            "compelled to answer you, or do as you bid, most will be curious enough to "
            "hear you out. You gain +20 on all Charm Animal and Animal Training Tests "
            "While this spell is active, you may only speak with beasts — you may not "
            "speak any civilised tongues, and can only communicate with your party"
            "using gestures or Language (Battle). Note, this also means you cannot "
            "cast any spells, or dispel, while Beast Tongue is active."
        ),
    },
    "Flock of Doom": {
        "CN": 8,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You call down a murder of crows or similar local bird to assail your "
            "foes. The flock attacks everyone in the Area of Effect who does not "
            "possess the Arcane Magic (Beasts) Talent ferociously, inflicting a +7 "
            "Damage hit at the end of the Round. The flock remains in play for the "
            "duration of the spell. For your Action you may make an Average (+20) "
            "Charm Animal Test to move the flock to another target within range. While "
            "within the Area of Effect, all creatures gain +1 Blinded Condition."
        ),
    },
    "Hunter’s Hide": {
        "CN": 6,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You cloak yourself in a shimmering mantle of Ghur. While the spell lasts, "
            "gain a bonus of +20 Toughness and the Dark Vision and Fear (1) Creature "
            "Traits (see page 339), as well as the Acute Sense (Smell) Talent."
        ),
    },
    "The Amber Spear": {
        "CN": 8,
        "range": " Willpower yards",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "You hurl a great spear of pure Ghur in a straight line. This is a magic "
            "missile with a Damage of +12. It strikes the first creature in its path, "
            "ignoring APs from armour made of leather and furs. If the target suffers "
            "any Wounds, also inflict +1 Bleeding Condition, after which the spear "
            "continues on its path, striking each target in the same manner, but at –1 "
            "Damage each time. If the spear fails to inflict any Wounds, its progress "
            "is stopped and the spell comes to an end. The Amber Spear only inflicts "
            "the minimum 1 Wound (see page 236) on the first target it strikes."
        ),
    },
    "Wyssan’s Wildform": {
        "CN": 8,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You call on the wild power of Ghur to infuse you, surrendering to its "
            "savage delights. Gain the following Creature Traits (see page 338): "
            "Arboreal, Armour (2), Belligerent, Big, Bite (Strength Bonus +1), Fear "
            "(1), Fury, Magical, Weapon (Strength Bonus +2). While the spell is in "
            "place you are incapable of using any Language or Lore skills."
        ),
    },
}

LORE_DEATH_DATA = {
    "Caress of Laniph": {
        "CN": 7,
        "range": "Touch",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "As you reach out your hand, it appears withered, even skeletal, drawing "
            "Shyish from your target’s corpus. This counts as a magic missile with a "
            "Damage of +6 that ignores Toughness Bonus and Armour Points. For every 2 "
            "Wounds inflicted, you may recover 1 Wound."
        ),
    },
    "Dying Words": {
        "CN": 6,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Touching the body of a recently departed soul (one that passed away "
            "within the last day), you call its soul back briefly. For the spell’s "
            "duration, you can communicate with the dead soul, though it cannot take "
            "any action other than talking. It is not compelled to answer you, but the "
            "dead do not lie."
        ),
    },
    "Purple Pall of Shyish": {
        "CN": 9,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You pull about you a pall fashioned from fine strands of purple magic. "
            "Gain +Willpower Bonus Armour Points on all locations, and the Fear (1) "
            "Creature Trait (see page 339). For every +2 SL you may increase your Fear "
            "rating by 1."
        ),
    },
    "Sanctify": {
        "CN": 10,
        "range": "Touch",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower minutes",
        "description": (
            "Inscribing a magical circle, you ward it with Shyish, forming an "
            "impenetrable barrier to the Undead. Creatures with the Undead Creature "
            "Trait cannot enter or leave the circle."
        ),
    },
    "Scythe of Shyish": {
        "CN": 6,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You conjure a magical scythe, which can be wielded in combat, using the "
            "Melee (Polearm) Skill. It acts like a normal scythe with a Damage equal "
            "to your Willpower Bonus+3. Enemies with the Undead Creature Trait do not "
            "receive Advantage when Engaged in combat with you."
        ),
    },
    "Soul Vortex": {
        "CN": 8,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Instant",
        "description": (
            "You hurl a shimmering ball of Shyish which erupts into purple flames, "
            "swirling with ghostly faces, mouths agape in silent terror. Targets "
            "within the Area of Effect receive +1 Broken Condition. Against targets "
            "with the Undead Creature Trait, Soul Vortex is a magic missile with a "
            "Damage of +10 that ignores Toughness Bonus and Armour Points."
        ),
    },
    "Steal Life": {
        "CN": 7,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "Thin strands of purple mist connect you briefly to your target, who "
            "wastes away before your very eyes. This counts as a magic missile with a "
            "Damage of +6 that ignores Armour Points and inflicts +1 Fatigued "
            "Condition. Further, you remove all Fatigued Conditions you currently "
            "suffer, and may heal yourself up to half the Wounds the target suffers, "
            "rounding up."
        ),
    },
    "Swift Passing": {
        "CN": 6,
        "range": "Touch",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "Your touch brings the release of death to a single mortally wounded "
            "target. If you successfully touch a target with 0 wounds remaining and at "
            "least 2 Critical Wounds, death swiftly follows. Further, the target "
            "cannot be raised as Undead."
        ),
    },
}

LORE_FIRE_DATA = {
    "Aqshy’s Aegis": {
        "CN": 5,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus rounds",
        "description": (
            "You wrap yourself in a fiery cloak of Aqshy, which channels flame into "
            "the Aegis. You are completely immune to damage from non-magical fire, "
            "including the breath attacks of monsters, and ignore any Ablaze "
            "Conditions you receive. You receive the Ward (9+) Creature Trait (see "
            "page 343) against magical fire attacks including spells from the Lore of "
            "Fire."
        ),
    },
    "Cauterise": {
        "CN": 4,
        "range": "Touch",
        "target": 1,
        "duration": "Instant",
        "description": (
            "Channelling Aqshy through your hands you lay them on an ally’s wounds. "
            "Immediately heal 1d10 Wounds and remove all Bleeding Conditions. Further, "
            "the wounds will not become infected. Targets without the Arcane Magic "
            "(Fire) Talent, must pass a Challenging (+0) Cool Test or scream in "
            "agony.. If Failed by –6 or more SL, the target gains the Unconscious "
            "Condition and is permanently scarred, waking up 1d10 hours later."
        ),
    },
    "Crown of Flame": {
        "CN": 8,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You channel Aqshy into a majestic crown of inspiring fire about your "
            "brow. Gain the Fear (1) Trait and +1 War Leader Talent while the spell is "
            "active. For every +2 SL, you may increase your Fear value by +1, or take "
            "War Leader Talent again. Furthermore, gain a bonus of +10 on all attempts "
            "to Channel and Cast with Aqshy while the spell is in effect."
        ),
    },
    "Flaming Hearts": {
        "CN": 8,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Your voice takes on a rich resonance, echoing with Aqshy’s fiery passion. "
            "Affected allies lose all Broken and Fatigued Conditions, and gain +1 "
            "Drilled, Fearless and Stout-hearted Talent while the spell is in effect."
        ),
    },
    "Firewall": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "AoE (Special)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You channel a fiery streak of Aqshy, creating a wall of flame. The "
            "Firewall is Willpower Bonus yards wide, and 1 yard deep. For every +2 SL "
            "you may extend the length of the Firewall by +Willpower Bonus yards. "
            "Anyone crossing the firewall gains 1 Ablaze condition and suffers a hit "
            "with a Damage equal to your Willpower Bonus, handled like a magical "
            "missile."
        ),
    },
    "Great Fires of U’Zhul": {
        "CN": 10,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You hurl a great, explosive blast of Aqshy into an enemy, which erupts "
            "into a furious blaze, burning with the heat of a forge. This is a magical "
            "missile with Damage +10 that ignores Armour Points and inflicts +2 Ablaze "
            "Conditions and the Prone Condition on a target. Everyone within the Area "
            "of Effect of that target suffers a Damage +5 hit ignoring Armour Points, "
            "and must pass a Dodge Test or also gain +1 Ablaze Condition. The spell "
            "stops behaving like a magic missile as the fire continues to burn in the "
            "Area of Effect for the duration. Anyone within the Area of Effect at the "
            "start of a round suffers 1d10+6 Damage, ignoring APs, and gains +1 Ablaze "
            "Condition."
        ),
    },
    "Flaming Sword of Rhuin": {
        "CN": 8,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wreathe a sword in magical flames. The weapon has Damage +6 and the "
            "Impact Quality (see page 298), and anyone struck by the blade gains +1 "
            "Ablaze Condition. If wielders do not possess the Arcane Magic (Fire) "
            "Talent, and they fumble an attack with the Flaming Sword, they gain +1 "
            "Ablaze Condition."
        ),
    },
    "Purge": {
        "CN": 10,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You funnel intense flame to burn away the taint and corruption in an "
            "area. Anything flammable is set alight, and any creatures in the area "
            "takes +SL Ablaze conditions. If the location contains a Corrupting "
            "Influence, such as Dhar, warpstone, or a Chaos- tainted object, it too "
            "will smoulder and blacken, beginning to burn. This spell may be "
            "maintained in subsequent rounds by passing a Challenging (+0) Channelling "
            "Test. The precise time needed to eliminate the Corrupting Influence will "
            "be determined by your GM. As a rough guideline, a small quantity (smaller "
            "than an acorn) of warpstone, or a minor Chaos-tainted object may require "
            "10–Willpower Bonus Rounds (minimum of 1 Round). A larger quantity of "
            "warpstone — fist-sized — or a more potent Chaos-tainted object may "
            "require double this. A powerful Chaos Artefact may take hours, or even "
            "longer… See page 182 for detail on Corrupting Influences."
        ),
    },
}

LORE_DEATH_DATA = {
    "Cerulean Shield": {
        "CN": 7,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You encase yourself in a crackling cage of sparking electricity and Azyr. "
            "For the spell’s duration, gain +SL Armour Points to all locations against "
            "melee attacks. If attacked by metal weapons — such as daggers, swords, "
            "and spears with metal tips — your attacker takes +Willpower Bonus Damage."
        ),
    },
    "Comet of Casandora": {
        "CN": 10,
        "range": "Initiative yards",
        "target": "AoE (Initiative Bonus yards)",
        "duration": "Special",
        "description": (
            "You channel all the Azyr you can muster and reach out to the skies, "
            "calling down a comet to wreak havoc amongst your foes. Select a target "
            "point within range. At the end of the next round, make an Average (+20) "
            "Perception Test. For every +SL you achieve, you may move your point of "
            "impact by Initiative Bonus yards. For every –SL, the GM will move the "
            "point of impact by Initiative Bonus yards in a random direction. Comet "
            "of Casandora then acts as a magical missile with Damage +12 that hits all "
            "targets in the Area of Effect, who also gain +1 Ablaze and the Prone "
            "Condition."
        ),
    },
    "Fate’s Fickle Fingers": {
        "CN": 6,
        "range": "You",
        "target": "AoE (Initiative Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "All allies within the Area of Effect, excluding those with the Arcane "
            "Magic (Heavens) Talent, create a single pool for their Fortune Points. "
            "All may draw on the pool, first come, first served. When the spell ends, "
            "you reallocate any remaining Fortune Points as fairly as possible."
        ),
    },
    "Starcrossed": {
        "CN": 7,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Initiative Bonus Rounds",
        "description": (
            "While this spell is active, you can spend Fortune Points to force an "
            "opponent to reroll Tests."
        ),
    },
    "T’Essla’s Arc": {
        "CN": 7,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "A crackling bolt of lightning shoots from your fingertips, striking your "
            "target. This is a magic missile with Damage +10 that inflicts +1 Blinded "
            "condition."
        ),
    },
    "The First Portent of Amul": {
        "CN": 3,
        "range": "You",
        "target": "You",
        "duration": "Initiative Bonus Rounds",
        "description": (
            "Gain +1 Fortune Point. For every +2 SL, gain +1 more. Any of these points "
            "unused at the end of the Duration are lost."
        ),
    },
    "The Second Portent of Amul": {
        "CN": 6,
        "range": "You",
        "target": "You",
        "duration": "Initiative Bonus Rounds",
        "description": (
            "Gain +SL Fortune Points. For every +2 SL, gain +1 additional Fortune "
            "point. Any unused points at the end of the Duration are lost."
        ),
    },
    "The Third Portent of Amul": {
        "CN": 12,
        "range": "You",
        "target": "You",
        "duration": "Initiative Bonus Rounds",
        "description": (
            "Gain +1 Fate Point. If the Fate point is not used by the end of the "
            "Duration, it is lost."
        ),
    },
}

LORE_METAL_DATA = {
    "Crucible of Chamon": {
        "CN": 7,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "You channel Chamon into a single non-magical, metallic object, such as a "
            "weapon or piece of armour. The item melts, dripping to the floor as "
            "molten metal, cooling almost immediately. If held, the item is dropped. "
            "If worn, the wearer takes a hit like a magic missile with Damage equal to "
            "your Willpower Bonus that ignores Toughness Bonus. While the object is "
            "destroyed, the metal retains its base value, and may be used by a smith "
            "as raw material."
        ),
    },
    "Enchant Weapon": {
        "CN": 6,
        "range": "Touch",
        "target": "special",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You encase a single non-magical weapon with heavy bands of Chamon, "
            "enhancing its potency. For the duration of the spell it counts as "
            "magical, gains a bonus to Damage equal to your Willpower Bonus, and gains "
            "the Unbreakable Quality (see page 298). For every +3 SL you may also add "
            "1 Quality or remove 1 Flaw from the weapon, while the spell is in effect."
        ),
    },
    "Feather of Lead": {
        "CN": 5,
        "range": "Willpower yards",
        "target": "Area of Effect (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Calling on the golden wind, you alter the density of your target’s "
            "belongings, raising or lowering their weight. For the duration of the "
            "spell, choose one effect for everyone within the area of effect: • Count "
            "as two steps more Overburdened • Do not count as Overburdened See page "
            "293 for details on Encumbrance."
        ),
    },
    "Fool’s Gold": {
        "CN": 4,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower minutes",
        "description": (
            "You weave Chamon into a non-magical object made of metal, fundamentally "
            "altering its alchemical nature. For the duration of the spell, all metal "
            "in the object becomes gold. This is not an illusion: it has actually "
            "transformed into gold. When the spell ends, the item reverts to its "
            "original metal. This spell can ruin good weapons, make armour too heavy "
            "to wear, and turn lead coins into something much more appealing. Spot "
            "effects arising from this spell are left in the hands of the GM."
        ),
    },
    "Forge of Chamon": {
        "CN": 9,
        "range": "Willpower Bonus yards",
        "target": "Special",
        "duration": "Willpower minutes",
        "description": (
            "You alter the quality of a single item made of metal. You may add 1 "
            "Quality or remove 1 Flaw. For every +2 SL, you may add another Quality or "
            "remove another Flaw."
        ),
    },
    "Glittering Robe": {
        "CN": 5,
        "range": "You",
        "target": "You",
        "duration": "Toughness Bonus Rounds",
        "description": (
            "Wild flurries of Chamon whirl around you, deflecting blows and "
            "intercepting missiles and magical attacks. Gain the Ward (9+) Creature "
            "Trait (see page 343) against all attacks and spells targeting you. Each "
            "hit successfully saved increases the Ward’s effectiveness by 1, to a "
            "maximum of Ward (3+)."
        ),
    },
    "Mutable Metal": {
        "CN": 5,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You touch a non-magical object made of metal, which instantly becomes "
            "warm to the touch as you squeeze Chamon into it. You may bend and mangle "
            "the object with an Average (+20) Strength Test. If you wish to make a "
            "more complex alteration, you may attempt an Average (+20) Trade (Smith, "
            "or similar) Test instead."
        ),
    },
    "Transmutation of Chamon": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wrench Chamon from the metals worn by your foes, and the earth "
            "itself, briefly transforming the flesh of your enemies into metal. This "
            "is a magic missile affecting all in the Area of Effect, with a Damage "
            "equal to your Willpower Bonus; the spell ignores Toughness Bonus and "
            "inflicts +1 Blinded, Deafened, and Stunned Condition, all of which last "
            "for the duration of the spell. All affected targets gain +1 Armour Point "
            "from the gold wrapped about their bodies, but also suffer from "
            "Suffocation (see page 181). If targets die while the spell is in effect, "
            "they are permanently encased in a shell of base metals, a macabre "
            "reminder of the risks of sorcery."
        ),
    },
}


LORE_LIFE_DATA = {
    "Barkskin": {
        "CN": 3,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You cause the target’s skin to become hard and rough like the bark of a "
            "tree. While affected by the spell, add +2 to the target’s Toughness "
            "Bonus, but suffer a penalty of –10 to Agility and Dexterity."
        ),
    },
    "Earthblood": {
        "CN": 6,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "To cast this spell, you must be in direct contact with the earth. "
            "Standing barefoot counts. For the duration of the spell, any creatures in "
            "direct contact with the earth within AoE heal Wounds equal to your "
            "Willpower Bonus at the start of every Round."
        ),
    },
    "Earthpool": {
        "CN": 8,
        "range": "You",
        "target": "You",
        "duration": "Instant",
        "description": (
            "On casting the spell, you immediately disappear into the ground in a wild "
            "torrent of Ghyran. You appear at the start of the next Round at any point "
            "within your Willpower in yards, erupting from the earth violently. For "
            "every +2 SL you may increase the distance travelled by your Willpower in "
            "yards. Any enemies engaged by you on your appearance gain the Surprised "
            "Condition. This spell will not allow you to move through stone but will "
            "allow you to move through water."
        ),
    },
    "Fat of the Land": {
        "CN": 4,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus days",
        "description": (
            "You flood the target’s body with nourishing Ghyran. The target need not "
            "eat or drink, but will still excrete as normal, though any leavings will "
            "be verdant green."
        ),
    },
    "Forest of Thorns": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "This spell may only target a patch of earth (though the patch can be very "
            "small). You cause a dense knot of wickedly spiked brambles and tangled "
            "vines to burst upwards, covering the Area of Effect. While the spell is "
            "active, anyone attempting to traverse the area on foot without the Arcane "
            "Magic (Life) Talent must make a Hard (–20) Agility Test. Failure means "
            "they gain 1 Bleeding Condition, and 1 Entangled Condition, with your "
            "Willpower used for its Strength. After the spell concludes, the growth "
            "remains, but loses its preternatural properties."
        ),
    },
    "Lie of the Land": {
        "CN": 5,
        "range": "Initiative Bonus miles",
        "target": "You",
        "duration": "Special",
        "description": (
            "Touching the earth, your senses flow through the Ghyran tracing the "
            "nearby area. After communing for 1 minute, you receive a detailed mental "
            "map of all-natural features — land, forests, rivers, but not settlements "
            "— within range. Settlements may be alluded to — areas of clear terrain, "
            "or dug trenches, for example. Each time you increase the range with SL "
            "increases the time taken communing with the land by +1 minute."
        ),
    },
    "Lifebloom": {
        "CN": 8,
        "range": "Willpower Bonus yards",
        "target": "Special",
        "duration": "Special",
        "description": (
            "You cause Ghyran to flood an area that is blighted or desolate. You may "
            "target either a dry riverbed, well, field, or a domestic animal. If you "
            "successfully cast the spell, the target bursts to life: • A dry river "
            "begins to flow once again • A dry or polluted well becomes clean and "
            "fresh • A planted field, vineyard or orchard bursts into life, with all "
            "crops immediately reaching full ripeness • A sick or unproductive animal "
            "becomes healthy. The affected beast is now healthily productive (cows "
            "produce milk, hens lay eggs, coats and hides of sheep and cows are "
            "healthy and lustrous) and any diseases are cured."
        ),
    },
    "Regenerate": {
        "CN": 6,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Your target gains the Regenerate Creature Trait (see page 341)."
        ),
    },
}

LORE_LIGHT_DATA = {
    "Banishment": {
        "CN": 12,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Instant",
        "description": (
            "You send a cleansing halo of Hysh out from hands, affecting all creatures "
            "within the Area of Effect whose Toughness is lower than your Willpower. "
            "Targets with the Undead and Daemonic Creature Traits gain the Unstable "
            "Creature Trait (see page 343). If they already have the Unstable Trait, "
            "they are reduced to 0 Wounds."
        ),
    },
    "Blinding Light": {
        "CN": 5,
        "range": "Willpower yards",
        "target": "You",
        "duration": "Instant",
        "description": (
            "You emit a bright, blinding flash of light from your hand or staff. "
            "Everyone looking at you, unless they possess the Arcane Magic (Light) "
            "Talent, receives +SL Blinded Conditions."
        ),
    },
    "Clarity of Thought": {
        "CN": 6,
        "range": "Touch",
        "target": 1,
        "duration": "Intelligence minutes",
        "description": (
            "You calm your target’s mind, allowing them to think clearly. All negative "
            "modifiers on their thinking processes — from Conditions, Mental "
            "Mutations, Psychologies, or any other source — are ignored while the "
            "spell is in effect."
        ),
    },
    "Daemonbane": {
        "CN": 10,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "You summon a blast of Hysh that passes through the border between the "
            "Realm of Chaos and the material world. The Casting Test is Opposed by the "
            "target making a Willpower Test. If you win, you obliterate a target with "
            "the Daemonic Creature Trait with a blinding white light, sending it back "
            "whence it came. If the spell successfully banishes a Daemon, everyone "
            "looking at your target, unless they possess the Arcane Magic (Light) "
            "Talent, receives +SL Blinded Conditions."
        ),
    },
    "Healing Light": {
        "CN": 9,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Instant",
        "description": (
            "Your target glows with a bright, cleansing light (equivalent light to a "
            "campfire), healing Intelligence Bonus + Willpower Bonus Wounds. If the "
            "Target passes a Very Hard (–20) Endurance Test, 1 Corruption point gained "
            "in the last hour is also lost."
        ),
    },
    "Net of Amyntok": {
        "CN": 8,
        "range": "Intelligence Bonus yards",
        "target": 1,
        "duration": "Target’s Intelligence Bonus Rounds",
        "description": (
            "You cast a delicate net woven from strands of Hysh over your targets, "
            "whose minds are overcome with conundrums and puzzles, leaving them "
            "paralysed with indecision. Targets gain +1 Stunned Condition, which they "
            "cannot lose while the spell is in effect. When recovering from the "
            "Condition, targets test their Intelligence instead of the Endurance "
            "Skill. Targets with the Bestial Creature Trait are immune to this spell."
        ),
    },
    "Phâ’s Protection": {
        "CN": 10,
        "range": "You",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You summon a protective aura of pure, holy light. Profane creatures — "
            "those with the Undead or Daemonic Creature Trait, those with mutations, "
            "and those with more Corruption than their Willpower Bonus and Toughness "
            "Bonus combined — cannot enter the Area of Effect. Any already within the "
            "Area gain the Broken Condition until they leave. Creatures within the "
            "Area cannot gain any Corruption points while the spell is active."
        ),
    },
    "Speed of Thought": {
        "CN": 8,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "A lattice of Hysh overlays your mind, allowing you to think rapidly. Gain "
            "a bonus of +20 to Intelligence and Initiative."
        ),
    },
}

LORE_SHADOWS_DATA = {
    "Choking Shadows": {
        "CN": 6,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wrap shadowy tendrils of Ulgu around your foes’ necks. Assuming they "
            "need to breathe, they gain +1 Fatigued Condition, cannot talk, and are "
            "subject to rules for Suffocation (see page 181)."
        ),
    },
    "Doppelganger": {
        "CN": 10,
        "range": "You",
        "target": "You",
        "duration": "Intelligence Bonus minutes",
        "description": (
            "You weave a mask and cloak of Ulgu around your form, assuming the "
            "likeness of another humanoid creature with whom you are familiar (as "
            "determined by the GM). Your appearance will automatically fool anyone "
            "without the Second Sight Talent, though some may note if any of your "
            "mannerisms are incorrect. Those with that Talent must pass a Difficult "
            "(–10) Perception Test to notice you are disguising your form. This does "
            "not let them see through the spell. They must dispel it to do so."
        ),
    },
    "Illusion": {
        "CN": 8,
        "range": "Willpower yards",
        "target": "AoE (Initiative Bonus yards)",
        "duration": "Willpower minutes",
        "description": (
            "You spin a web of intricate strands of Ulgu, obfuscating the Area of "
            "Effect with an illusory image of your choosing. You will automatically "
            "fool anyone without the Second Sight Talent. Those with that Talent must "
            "pass a Difficult (–10) Perception Test to notice the illusion. This does "
            "not let them see through the spell. They must dispel it to do so. The "
            "illusion is, by default, static. For your Action, you may make a Hard "
            "(–20) Channelling Test to make the illusion move for that Round."
        ),
    },
    "Mindslip": {
        "CN": 6,
        "range": "1 yard",
        "target": 1,
        "duration": "Willpower minutes",
        "description": (
            "You conjure delicate threads of Ulgu in your Target’s mind, causing all "
            "prior memory of you to disappear for the spell’s duration. Once the spell "
            "is over, the Target must pass an Average (+20) Intelligence Test, or the "
            "memory loss becomes permanent until dispelled."
        ),
    },
    "Mystifying Miasma": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "AoE (Willpower Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You conjure forth a swirling mass of mist shot through with roiling "
            "shadow that flits and confounds the senses. Anyone within the mist who "
            "does not possess the Arcane Magic (Shadows) Talent is affected by the "
            "Miasma, gaining +1 Blinded, Deafened, and Fatigued Condition, which "
            "remain for the spell’s duration. Anyone affected attempting to move must "
            "pass a Challenging (+0) Perception Test, or gain the Prone Condition. If "
            "the spell is dispelled once in play, anyone affected by the spell must "
            "make a Routine (+40) Initiative Test, or gain the Stunned Condition."
        ),
    },
    "Shadowsteed": {
        "CN": 6,
        "range": "Willpower Bonus yards",
        "target": 1,
        "duration": "Until the next sunrise",
        "description": (
            "You summon forth a shadowy steed. The creature’s unnatural flesh is black "
            "as midnight, and at times it appears to be both solid and insubstantial. "
            "Use the rules for a riding horse. When the Shadowsteed is out of "
            "sunlight, it also gains the following Creature Traits: Dark Vision, "
            "Ethereal, Magical, Painless, Stealthy, Stride, Fear (1) and Ward (+9) . "
            "Even when insubstantial, Shadowsteeds may be ridden. Riders with the "
            "Arcane Magic (Shadow) Talent do so with a bonus of +20 to Ride Tests. "
            "Those without suffer a penalty of –20 to Ride Tests. Shadowsteeds are "
            "tireless, so need no rest (though their unsettled riders might!). As the "
            "first rays of dawn break over the horizon the steeds melt into "
            "insubstantial mist. If still being ridden when the spell ends, or when "
            "dispelled, the rider will suffer Falling Damage (see page 166)."
        ),
    },
    "Shadowstep": {
        "CN": 8,
        "range": "Willpower yards",
        "target": "You",
        "duration": "Instant",
        "description": (
            "You create a shadowy portal of Ulgu through the aethyr. You disappear "
            "from your current location and immediately appear up to your Willpower "
            "yards away. Any enemies Engaged by you on your disappearance or "
            "reappearance gain the Surprised Condition."
        ),
    },
    "Shroud of Invisibility": {
        "CN": 8,
        "range": "Touch",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You wrap the target in a shroud of Ulgu. The Target becomes invisible and "
            "cannot be perceived by mundane senses. The spell will automatically fool "
            "anyone without the Second Sight Talent. Those with the Talent must pass a "
            "Challenging (+0) Perception Test to notice that someone is nearby, though "
            "they will not be able to pin down the precise location. They must dispel "
            "the Shroud of Invisibility to do so . You are still perceptible to the "
            "other senses, and the spell will come to an end if you bring attention to "
            "yourself by making large noises or attacking someone."
        ),
    },
}

LORE_HEDGECRAFT_DATA = {
    "Goodwill": {
        "CN": 0,
        "range": "You",
        "target": "AoE (Fellowship Bonus yards)",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You create an atmosphere conducive to friendliness and good spirits. All "
            "Fellowship Tests within the Area of Effect receive a bonus of +10, and "
            "Animosity and Hatred Psychologies have no effect."
        ),
    },
    "Mirkride": {
        "CN": 0,
        "range": "You",
        "target": "You",
        "duration": "Willpower Bonus minutes",
        "description": (
            "Speaking ancient words of magic, your spirit leaves your body, stepping "
            "into the Hedge, the dark space between the material world and the spirit "
            "realm. For the duration, your stand apart from the world, able to witness "
            "it invisibly, but not affect it in any way. Physical barriers are no "
            "impediment to you, and you may walk through non-magical obstacles at "
            "will. Your body remains in place, immobile and insensate. At the end of "
            "the spell you will be pulled suddenly back to your body. If your body is "
            "killed while you are walking the Hedge, your spirit will wander aimlessly "
            "for eternity."
        ),
    },
    "Nepenthe": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You mutter words of power over a premade potion of herbs, magically "
            "transforming it into a potent philtre. If drunk while the spell is in "
            "effect, the target may choose to completely forget one individual, "
            "permanently."
        ),
    },
    "Nostrum": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You incant a spell over an already prepared draught, imbuing it with "
            "magical power. If drunk while the spell is in effect, the target "
            "immediately heals your Willpower Bonus in Wounds and is cured of one "
            "disease. For every +2 SL you may cure an extra disease."
        ),
    },
    "Part the Branches": {
        "CN": 0,
        "range": "You",
        "target": "You",
        "duration": "Willpower minutes",
        "description": (
            "Your pupils dilate as you complete your incantation, and you are able to "
            "see into the Spirit world. This allows you to perceive invisible "
            "creatures, spirits, and Daemons, even those marked as impossible to see."
        ),
    },
    "Protective Charm": {
        "CN": 0,
        "range": "Touch",
        "target": "Special",
        "duration": "Willpower Bonus days",
        "description": (
            "You imbue a protective charm with a spell of protection. Those bearing "
            "the charm gain the Magic Resistance Talent. If they already have that "
            "Talent, the charm does nothing more."
        ),
    },
}

LORE_WITCHCRAFT_DATA = {
    "Blight": {
        "CN": 14,
        "range": "Willpower Bonus yards",
        "target": "Special",
        "duration": "Special",
        "description": (
            "You may target either a well, a field, or a domestic animal. If you "
            "successfully cast the spell, the target suffers from a blight: "
            "• A blighted well becomes instantly brackish and stagnant "
            "• Any crops currently planted in a Blighted field rot overnight "
            "• A blighted animal sickens. The afflicted beast no longer produces "
            "anything (cows produce no milk, hens produce no eggs, coats and hides "
            "grow mangy and unusable) and will die in 10–SL days"
        ),
    },
    "Creeping Menace": {
        "CN": 6,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "You summon a swarm of creeping, slithering creatures to harass your foes. "
            "Each target affected is immediately engaged by a swarm of Giant Rats, "
            "Giant Spiders, or Snakes. Use the standard profiles for the relevant "
            "creature type, adding the Swarm Trait. For your Action you may make a "
            "Challenging (+0) Charm Animal Test to direct 1 or more swarms to attack a "
            "different target. When the spell ends, any remaining swarms disappear "
            "into the shadows."
        ),
    },
    "Curse of Crippling Pain": {
        "CN": 10,
        "range": "Willpower yards",
        "target": 1,
        "duration": "Willpower Bonus Rounds",
        "description": (
            "Stabbing a crude representation of your target — a doll or puppet — you "
            "inflict crippling pain. When successfully cast, choose which hit location "
            "to stab: "
            "• Leg – Leg becomes useless, as if it was Amputated (see page 180). If "
            "running, the target also gains the Prone Condition and takes falling "
            "Damage. "
            "• Arm – Arm becomes useless, as if it was Amputated (see page 180). If "
            "target was holding anything in that hand, it is automatically dropped. "
            "• Body – Target doubles up in agony, gaining +1 Fatigued Condition, and "
            "must pass a Hard (–20) Endurance Test or gain the Prone Condition. "
            "• Head – Target gains the Stunned Condition, and must pass an Average "
            "(+20) Endurance Test or gain the Unconscious Condition for the Duration. "
            "While the spell is in effect, for your Action you may make a Channelling "
            "Test, stabbing the doll again, to affect a different location."
        ),
    },
    "Curse of Ill-Fortune": {
        "CN": 8,
        "range": "Willpower Bonus miles",
        "target": 1,
        "duration": "Willpower Bonus days",
        "description": (
            "The ingredient for this spell is something belonging to the target, "
            "either a personal possession or a strand of hair. For the duration, your "
            "target suffers bad luck. Laces snap, chairs break, and other minor "
            "narrative effects inconvenience them. The target suffers a penalty of –10 "
            "to all Tests, in addition to any other modifiers, and may not spend "
            "Fortune points."
        ),
    },
    "Haunting Horror": {
        "CN": 8,
        "range": "Touch",
        "target": "AoE (a single location)",
        "duration": "Willpower days",
        "description": (
            "You target a single location, such as a house or clearing, and inflict "
            "haunting dreams and waking nightmares on any who enter there. Those "
            "entering while the spell is in effect are unnerved by eerie sensations, "
            "flitting shadows, and whispered voices lurking on the threshold of "
            "hearing. Unless they possess the Arcane Magic (Witchcraft) Talent, they "
            "gain +1 Fatigued Condition. Then, unless they pass an Challenging (+0) "
            "Cool Test, they gain another +1 Fatigued Condition and the Broken "
            "Condition, both of which are only removed upon leaving the location."
        ),
    },
    "The Evil Eye": {
        "CN": 6,
        "range": "Willpower yards",
        "target": "Special",
        "duration": "Instant",
        "description": (
            "You lock eyes with a single target, who must be looking at you. Perform "
            "an Opposed Intimidate/Cool Test, adding any SL from your casting roll to "
            "your result. Your opponent gains 1 Fatigued Condition per +2 SL by which "
            "you win. If you win by 6+ SL, your opponent gains the Broken Condition."
        ),
    },
}
