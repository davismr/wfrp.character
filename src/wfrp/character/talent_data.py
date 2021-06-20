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
        "description": "Attempt an Opposed Charm/Intelligence Test. Success gives your opponent a Stunned Condition. Further, for each level you have in Blather, your opponent gains another Stunned Condition. Targets Stunned by Blather may do nothing other than stare at you dumbfounded as they try to catch-up with or understand what you are saying..."
    },
    "Concoct": {
        "description": "You are skilled at making potions, philtres, and draughts on the go. You may take one free Crafting Endeavour to use Lore (Apothecary) without need of a Workshop. Other Crafting Endeavours use the normal rules.",
    },
    "Contortionist": {
        "description": "You can bend and manipulate your body in a myriad of seemingly unnatural ways. This allows you to squeeze through unlikely gaps and bend your body in crazy ways, giving benefits determined by the GM, possibly with a successful Agility test.",
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
    "Criminal": {
        "description": "You are an active criminal making money from illegal sources, and you’re not always quiet about it..."
    },
    "Deadeye Shot": {
        "description": "You always hit an opponent right between the eyes... or wherever else you intended to hit. Instead of reversing the dice to determine which Hit Location is struck with your ranged weapons, you may pick a location."
    },
    "Dealmaker": {
        "description": "You are a skilled businessman who knows how to close a deal. When using the Haggle skill, you reduce or increase the price of the products by an extra 10%."
    },
    "Detect Artefact": {
        "description": "You are able to sense when magic lies within an artefact. You may attempt an Intuition Test for any magical artefact touched. If successful, you sense the item is magical; further, each SL also provides a specific special rule the item uses, if it has any. Normally, you may only attempt this Test once per artefact touched."
    },
    "Diceman": {
        "description": "You are a dicing master, and all claims you cheat are clearly wrong. When you successfully use Gamble or Sleight of Hand when playing with dice, you can choose to either use your rolled SL, or the number rolled on your units die. So, a successful roll of 06 could be used for +6 SL. If you play any real-life dice games to represent in-game dice games, always roll extra dice equal to your Diceman level and choose the best results."
    },
    "Dirty Fighting": {
        "description": "You have been taught all the dirty tricks of unarmed combat. You may choose to cause an extra +1 Damage for each level in Dirty Fighting with any successful Melee (Brawling) hit."
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
    "In-fighter": {
        "description": "You are skilled at drawing in close to an opponent. You suffer no penalties for fighting against an opponent with a longer weapon than you. Further, if you use the optional rules for In-fighting (see page 297), gain a bonus of +10 to hit your opponent."
    },
    "Inspiring": {
        "description": "Your rousing words and pleas can turn the tide of a battle. Refer to the following table to see how many people you can now influence with your Leadership Skill (see page 126) when at war."
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
    "Slayer": {
        "description": "When determining Damage use your opponent’s Toughness Bonus as your Strength Bonus if it is higher; always determine this before any other rules modify your Strength or Strength Bonus. Further, if your target is larger than you, and your score a Critical (see page 159), multiply all melee Damage you cause by the number of steps larger your target is (so, 2 steps = ×2, 3 steps = ×3, and so on); this multiplication is calculated after all modifiers are applied. See page 341 for more about Size."
    },
    "Small": {
        "description": "You are much shorter than most folk in the Old World. The full rules for different Sizes are found in Chapter 12: Bestiary on page 341."
    },
    "Sniper": {
        "description": "Distance is of no import to your shooting skills, and you are just as adept at picking off far away targets as those nearby. You suffer no penalties for shooting at Long range, and half the penalties for Extreme range."
    },
    "Speedreader": {
        "description": "You read books at a voracious pace. You may reverse a failed Research Test if this will grant success. If the speed at which you read is important during combat, a successful Language Test lets you read and fully comprehend a number of pages per Round equal to your SL plus Speedreader level (minimum of 1, even if you fail the Test)."
    },
    "Sprinter": {
        "description": "You are a swift runner. Your Movement Attribute counts as 1 higher when Running."
    },
    "Step Aside": {
        "description": "You are skilled at being where enemy weapons are not. If you use Dodge to defend against an incoming attack and win the Opposed Test, you may move up to 2 yards as you dive away, and no longer count as Engaged. None of your opponents will gain a Free Attack when you do this."
    },
    "Stone Soup": {
        "description": "You are used to getting by with less, and know how to survive lean times. You can subsist on half the amount of food required without any negative penalties (bar feeling really hungry), and need only test for Starvation every 3 days, not 2 (see page 181)."
    },
    "Stout-hearted": {
        "description": "No matter how bad things get, you always seem to come back for more. You may attempt a Cool Test to remove a Broken Condition at the end of each of your Turns as well as at the end of the Round (see page 168 for more on this)."
    },
    "Strider": {
        "description": "You are experienced in traversing difficult ground. You ignore all movement penalties when crossing over or through a specified terrain. Typical specialities include: Coastal, Deserts, Marshes, Rocky, Tundra, Woodlands.",
        "specialisations": [
            "Coastal",
            "Deserts",
            "Marshes",
            "Rocky",
            "Tundra",
            "Woodlands",
        ],
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
    "Suave": {
        "description": "You gain a permanent +5 bonus to your starting Fellowship Characteristic (this does not count towards your Advances)."
    },
    "Super Numerate": {
        "description": "You have a gift for calculation and can work out the solution to most mathematical problems with ease. You may use a simple calculator to represent what your PC is capable of mentally computing."
    },
    "Supportive": {
        "description": "You know what to say and when to make the most impact upon your superiors. When you successfully use a social Skill to influence those with a higher Status tier, you can choose to either use your rolled SL, or the number rolled on your units die. So, a successful roll of 46 could be used for +6 SL."
    },
    "Sure Shot": {
        "description": "You know how to find the weak spots in a target’s armour. When you hit a target with a Ranged weapon, you may ignore Armour Points equal to your Sure Shot level."
    },
    "Surgery": {
        "description": "You are a surgeon, able to open and close the flesh in order to heal others. You can treat any Critical Wound marked as needing Surgery. You can also perform surgery to resolve internal issues with an Extended Challenging (+0) Heal Test with a target SL determined by the GM (usually 5–10) depending upon the difficulty of the procedure at hand. This will cause 1d10 Wounds and 1 Bleeding Condition per Test, meaning surgery has a high chance of killing a patient if the surgeon is not careful. After surgery, the patient must pass an Average (+20) Endurance Test or gain a Minor Infection (see page 187)."
    },
    "Tenacious": {
        "description": "You never give up, no matter how impossible your travails appear. You can double the length of time successful Endurance Tests allow you to endure a hardship. This includes enduring prolonged riding, exposure, rituals, and similar adversities."
    },
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
