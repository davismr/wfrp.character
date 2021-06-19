def get_random_talent(die_roll):
    while True:
        try:
            return TALENT_LIST[die_roll]
        except KeyError:
            die_roll += 1


TALENT_LIST = {
    3: "Acute Sense (any one)",
    6: "Ambidextrous",
    9: "Animal Affinity",
    12: "Artistic",
    15: "Attractive",
    18: "Coolheaded",
    21: "Craftsman (any one)",
    24: "Flee!",
    28: "Hardy",
    31: "Lightning Reflexes",
    34: "Linguistics",
    38: "Luck",
    41: "Marksman",
    44: "Mimic",
    47: "Night Vision",
    50: "Nimble Fingered",
    52: "Noble Blood",
    55: "Orientation",
    58: "Perfect Pitch",
    62: "Pure Soul",
    65: "Read/Write",
    68: "Resistance (any one)",
    71: "Savvy",
    74: "Sharp",
    78: "Sixth Sense",
    81: "Strong Legs",
    84: "Sturdy",
    87: "Suave",
    91: "Super Numerate",
    94: "Very Resilient",
    97: "Very Strong",
    100: "Warrior Born",
}
TALENT_DATA = {
    "Accurate Shot": {
        "description": "You are an exceptional shot and know where to shoot an enemy in order to inflict maximum damage. You deal your Accurate Shot level in extra Damage with all ranged weapons."
    },
    "Acute Sense": {
        "description": "One of your primary five senses is highly developed, allowing you to spot what others miss. You may take Perception Tests to detect normally imperceptible details with the associated sense, as dictated by the GM. This could include: seeing an eagle beyond everyone else’s eyeshot, smelling an almost odourless poison, hearing the breath of an unmoving mouse within a wall, feeling a worn away letter in a carving, or tasting that two beers from the same brewer have been drawn from two different barrels.",
        "specialisations": [
            "Touch",
            "Sight",
            "Hearing",
            "Smell",
            "Taste",
        ],
    },
    "Aethyric Attunement": {
        "description": "Your experience, talent or training lets you more safely manipulate the Winds of Magic. You do not suffer a Miscast if you roll a double on a successful Channel Test."
    },
    "Ambidextrous": {
        "description": "You can use your off-hand far better than most folk, either by training or innate talent. You only suffer a penalty of –10 to Tests relying solely on your secondary hand, not –20. If you have this Talent twice, you suffer no penalty at all."
    },
    "Animal Affinity": {"description": ""},
    "Artistic": {"description": ""},
    "Attractive": {"description": ""},
    "Beat Blade": {
        "description": "You are trained to make sharp controlled blows to your opponent’s weapon, creating an opening for an attack or simply impeding an incoming attack. For your Action, you can choose to Beat Blade before rolling. Perform a Melee Test; if successful, your opponent loses –1 Advantage, and loses a further –1 per SL you score. This Test is not Opposed. This Talent is of no use if your opponent has no weapon, or has a larger Size than you (see page 341)."
    },
    "Beneath Notice": {
        "description": "The high and mighty pay no attention to your presence, knowing you are well beneath their notice. Assuming you are properly attired and not in an incongruous position, those of a higher Status Tier will normally ignore you unless your presence becomes inappropriate, which can make it very easy to listen into conversations you perhaps shouldn’t. Further, characters with a higher Status Tier than you gain no Advantage for striking or wounding you in combat, as there is nothing to be gained for defeating such a lowly cur."
    },
    "Blather": {
        "description": "Attempt an Opposed Charm/Intelligence Test. Success gives your opponent a Stunned Condition. Further, for each level you have in Blather, your opponent gains another Stunned Condition. Targets Stunned by Blather may do nothing other than stare at you dumbfounded as they try to catch-up with or understand what you are saying. "
    },
    "Coolheaded": {
        "max": 1,
        "description": "You gain a permanent +5 bonus to your starting Willpower Characteristic this does not count towards your Advances.",
    },
    "Crack the Whip": {
        "description": "You know how to get the most out of your animals. When an animal you control is Fleeing or Running, it gains +1 Movement if you are using a whip.",
    },
    "Craftsman": {
        "description": "You have true creative talent. Add the associated Trade Skill to any Career you enter. If the Trade Skill is already in your Career, you may instead purchase the Skill for 5 XP fewer per Advance.",
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
    "Disarm": {
        "description": "You are able to disarm an opponent with a careful flick of the wrist or a well-aimed blow to the hand."
    },
    "Doomed": {
        "description": "At the age of 10, a Priest of Morr called a Doomsayer took you aside to foretell your death in an incense-laden, coming-of-age ritual called the Dooming. In conjunction with your GM, come up with a suitable Dooming. Should your character die in a fashion that matches your Dooming, your next character gains a bonus of half the total XP your dead character accrued during play."
    },
    "Etiquette": {
        "description": "You can blend in socially with the chosen group so long as you are dressed and acting appropriately. Example social groups for this Talent are: Criminals, Cultists, Guilders, Nobles, Scholars, Servants, and Soldiers. If you do not have the Talent, those with it will note your discomfort in the unfamiliar environment. This is primarily a matter for roleplaying, but may confer a bonus to Fellowship Tests at the GM’s discretion.",
        "specialisations": [
            "Criminals",
            "Cultists",
            "Guilders",
            "Nobles",
            "Scholars",
            "Servants",
            "Soldiers",
        ],
    },
    "Flee!": {
        "description": "When your life is on the line you are capable of impressive bursts of speed. Your Movement Attribute counts as 1 higher when Fleeing (see page 165)."
    },
    "Gregarious": {
        "description": "You just like talking to other folk and it seems they like talking to you. You may reverse any failed Gossip Test if this allows the Test to succeed."
    },
    "Gunner": {
        "description": "You can reload blackpowder weapons with practiced ease. Add SL equal to your level in Gunner to any Extended Test to reload a Blackpowder weapon."
    },
    "Hardy": {
        "description": "You gain a permanent addition to your Wounds, equal to your Toughness Bonus. If your Toughness Bonus should increase, then the number of Wounds Hardy provides also increases."
    },
    "Hatred": {
        "description": "You are consumed with hatred for something in the Old World, as described on page 190. Each time you take this Talent you develop hatred for a new group. Examples you could take include: Beastmen, Greenskins, Monsters, Outlaws, Sigmarites, Undead, Witches.",
        "specialisations": [
            "Beastmen",
            "Greenskins",
            "Monsters",
            "Outlaws",
            "Sigmarites",
            "Undead",
            "Witches",
        ],
    },
    "Holy Hatred": {
        "description": "Your prayers drip with the hatred you feel for your blasphemous enemies. You deal +1 Damage with Miracles for each level in this Talent."
    },
    "Holy Visions": {
        "description": "You clearly see the great works of the Gods all around you. You automatically know when you enter Holy Ground, and may take anIntuitionTesttoreceivevisions(oftenobscure,andseenthrough the paradigm of your cult or individual belief-system) regarding the local area if significant events have occurred there in the past."
    },
    "Lightning Reflexes": {"description": ""},
    "Linguistics": {"description": ""},
    "Luck": {"description": ""},
    "Magic Resistance": {
        "description": "The SL of any spell affecting you is reduced by 2 per point you have in this Talent."
    },
    "Marksman": {"description": ""},
    "Mimic": {"description": ""},
    "Night Vision": {
        "description": "You can see very well in natural darkness. Assuming you have at least a faint source of light (such as starlight, moonlight, or bioluminescence) you can see clearly for 20 yards per level of Night Vision. Further, you can extend the effective illumination distance of any light sources by 20 yards per level of Night Vision."
    },
    "Nimble Fingered": {"description": ""},
    "Noble Blood": {"description": ""},
    "Orientation": {"description": ""},
    "Perfect Pitch": {"description": ""},
    "Pure Soul": {
        "description": "Your soul is pure, quite resistant to the depredations of Chaos. You may gain extra Corruption points equal to your level of Pure Soul before having to Test to see if you become corrupt."
    },
    "Read/Write": {
        "description": "You are one of the rare literate individuals in the Old World. You are assumed to be able to read and write (if appropriate) all of the Languages you can speak."
    },
    "Relentless": {
        "description": "When you have your mind set on a target, there is nothing anyone can do to stop you reaching them. If you use Advantage when Disengaging, you may keep a number of Advantage equal to your level of Relentless. Further, you may use Advantage to Disengage even if you have lower Advantage than your opponents."
    },
    "Resistance": {
        "description": "Your strong constitution allows you to more readily survive a specific threat. You may automatically pass the first Test to resist the specified threat, such as Magic, Poison, Disease, Mutation, every session. If SL is important, use your Toughness Bonus as SL for the Test.",
        "specialisations": ["Magic", "Poison", "Disease", "Mutation"],
    },
    "Roughrider": {
        "description": "You are at home in the saddle in even the most difficult of circumstances, and know how to get the best out of your mount during conflict. Assuming you have the Ride skill, you can direct your mount to take an Action, not just a Move, without a Ride test."
    },
    "Rover": {
        "description": "You are at home roaming the wild places. When using Stealth in a rural environment, bystanders do not get passive Perception Tests to detect you; they can only spot you if they are specifically on look-out, or watching for hidden spies."
    },
    "Savvy": {
        "description": "You gain a permanent +5 bonus to your starting Intelligence Characteristic (this does not count towards your Advances)"
    },
    "Sharp": {
        "description": "You gain a permanent +5 bonus to your starting Initiative Characteristic (this does not count towards your Advances)."
    },
    "Sixth Sense": {
        "description": "You get a strange feeling when you are threatened, and can react accordingly. The GM may warn you if you are walking into danger; this will normally come after a secret Intuition Test on your behalf. Further, you may ignore Surprise if you pass an Intuition Test."
    },
    "Strike Mighty Blow": {
        "description": "You know how to hit hard! You deal your level of Strike Mighty Blow in extra Damage with melee weapons."
    },
    "Strike to Injure": {
        "description": "You are an expert at striking your enemies most vulnerable areas. You inflict your level of Strike to Injure in additional Wounds when you cause a Critical Wound."
    },
    "Strike to Stun": {
        "description": "You know where to hit an opponent to bring him down fast. You ignore the ‘Called Shot’ penalty to strike the Head Hit Location when using a melee weapon with the Pummel Quality (see page 298). Further, you count all improvised weapons as having the Pummel Quality."
    },
    "Strong Back": {
        "description": "You have a strong back that is used to hard work. You may add your levels in Strong Back to your SL in any Opposed Strength Tests, and can carry additional Encumbrance points of trappings (see page 293) equal to your level of Strong Back."
    },
    "Strong Legs": {
        "description": "You have strong legs able to carry you great distances when you jump. Add your Strong Legs level to your SL in any Athletics Tests involving Leaping (see page 166)."
    },
    "Strong-minded": {
        "description": "You are the epitome of determination and resolve. Add your level in Strong Minded to your maximum Resolve pool."
    },
    "Strong Swimmer": {
        "description": "You are an especially strong swimmer and used to holding your breath for a long time underwater. Gain a bonus of your level in Strong Swimmer to your Toughness Bonus for the purposes of holding your breath."
    },
    "Sturdy": {
        "description": "You have a brawny physique, or are very used to carrying things. Increase the number of Encumbrance Points you can carry by your Sturdy level x 2."
    },
    "Suave": {"description": ""},
    "Super Numerate": {"description": ""},
    "Very Resilient": {"description": ""},
    "Very Strong": {"description": ""},
    "Warrior Born": {
        "description": "You gain a permanent +5 bonus to your starting Weapon Skill Characteristic (doesn’t count as Advances)."
    },
    "Waterman": {
        "description": "You are an experienced freshwater sailor and are well-versed with river vessels. You can ignore all negatives to your Tests when onboard a barge derived from rolling waters, swaying vessels, unsure footing, and similar. Further, you count as two boatmen towards the minimum number of crew to pilot a river vessel."
    },
    "Wealthy": {
        "description": "You are fabulously wealthy, and are rarely ever short of coin. When Earning (including Income Endeavours) you secure +1 GC per time you have this Talent."
    },
    "Well-prepared": {
        "description": "You are used to anticipating the needs of others, and yourself. A number of times per session equal to your level of Well-Prepared, you may pull the trapping required for the current situation from your backpack (or similar) as long as it is Encumbrance 0, could feasibly been bought recently, and doesn’t stretch credibility too far. This could be anything from a flask of spirits to fortify a wounded comrade to a pfennig-whistle needed by a passing entertainer. Whenever you do this, you must deduct the cost for the prepared item from your purse, representing the coin you spent earlier."
    },
    "Witch!": {
        "description": "You have learned magic through trial and error. Add Language (Magick) to any Career you enter; if it is already in your Career, you may purchase the Skill for 5 XP fewer per Advance. Further, you may spend 1 Resilience point to immediately cast any spell as if it were one of your Arcane Lore spells; you also instantly memorise that spell as one of your Arcane Lore spells for 0 XP. You can do this a number of times equal to your level in this Talent."
    },
}
