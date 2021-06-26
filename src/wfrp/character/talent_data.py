def get_random_talent(die_roll):
    while True:
        try:
            return TALENT_LIST[die_roll]
        except KeyError:
            die_roll += 1


TALENT_LIST = {
    3: "Acute Sense (Any)",
    6: "Ambidextrous",
    9: "Animal Affinity",
    12: "Artistic",
    15: "Attractive",
    18: "Coolheaded",
    21: "Craftsman (Any)",
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
    68: "Resistance (Any)",
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
    "Alley Cat": {
        "description": "You are at home in shadowy backstreets. When using Stealth (Urban), you may reverse the dice of any failed Test if this will score a Success."
    },
    "Ambidextrous": {
        "description": "You can use your off-hand far better than most folk, either by training or innate talent. You only suffer a penalty of –10 to Tests relying solely on your secondary hand, not –20. If you have this Talent twice, you suffer no penalty at all."
    },
    "Animal Affinity": {
        "description": "You have a natural talent for art, able to produce precise sketches with nothing but time and appropriate media. This ability has several in-game uses, ranging from creating Wanted Posters to sketching accurate journals, and has spot benefits as determined by the GM. Further to this, add Art (Any) to any Career you enter; if it is already in Career, you may instead purchase the Skill for 5 XP fewer per Advance."
    },
    "Artistic": {
        "description": "You have a natural talent for art, able to produce precise sketches with nothing but time and appropriate media. This ability has several in-game uses, ranging from creating Wanted Posters to sketching accurate journals, and has spot benefits as determined by the GM. Further to this, add Art (Any) to any Career you enter; if it is already in Career, you may instead purchase the Skill for 5 XP fewer per Advance."
    },
    "Attractive": {
        "description": "Whether it’s your piercing eyes, your strong frame, or maybe the way you flash your perfect teeth, you know how to make the best use of what the gods gave you. When you successfully use Charm to influence those attracted to you, you can choose to either use your rolled SL, or the number rolled on your units die. So, a successful roll of 38 could be used for +8 SL."
    },
    "Beat Blade": {
        "description": "You are trained to make sharp controlled blows to your opponent’s weapon, creating an opening for an attack or simply impeding an incoming attack. For your Action, you can choose to Beat Blade before rolling. Perform a Melee Test; if successful, your opponent loses –1 Advantage, and loses a further –1 per SL you score. This Test is not Opposed. This Talent is of no use if your opponent has no weapon, or has a larger Size than you (see page 341)."
    },
    "Beneath Notice": {
        "description": "The high and mighty pay no attention to your presence, knowing you are well beneath their notice. Assuming you are properly attired and not in an incongruous position, those of a higher Status Tier will normally ignore you unless your presence becomes inappropriate, which can make it very easy to listen into conversations you perhaps shouldn’t. Further, characters with a higher Status Tier than you gain no Advantage for striking or wounding you in combat, as there is nothing to be gained for defeating such a lowly cur."
    },
    "Berserk Charge": {
        "description": "You hurl yourself at your enemies with reckless abandon, using the force of your charge to add weight to your strikes. When you Charge, you gain +1 Damage to all Melee attacks per level in this Talent."
    },
    "Blather": {
        "description": "Attempt an Opposed Charm/Intelligence Test. Success gives your opponent a Stunned Condition. Further, for each level you have in Blather, your opponent gains another Stunned Condition. Targets Stunned by Blather may do nothing other than stare at you dumbfounded as they try to catch-up with or understand what you are saying..."
    },
    "Bless": {
        "description": "You are watched over by one of the Gods and can empower simple prayers. You can now deploy the Blessings of your deity as listed in Chapter 7: Religion and Belief. Under normal circumstances, you may only ever know one Divine Lore for the Bless Talent."
    },
    "Bookish": {
        "description": "You are as at home in a library as a seaman at sea or a farmer a-farming. When using Research, you may reverse the dice of any failed Test if this will score a success."
    },
    "Break and Enter": {
        "description": "You are an expert at quickly breaking down doors and forcing entry. You may add +1 Damage for each level in this Talent when determining damage against inanimate objects such as windows, chests, doors, and similar."
    },
    "Briber": {
        "description": "You are an exceedingly skilled briber. The GM should reduce the base cost of any required bribe by 10% per level you have in Briber, to a minimum of 10% of the original amount."
    },
    "Cardsharp": {
        "description": "You are used to playing, and winning, at cards, although your methods may involve a little cheating. When you successfully use Gamble or Sleight of Hand when playing cards, you can choose to either use your rolled SL, or the number rolled on your units die. So, a successful roll of 28 could be used for +8 SL. If you play a real card game to represent what is happening in-game, you may receive an extra number of cards per deal equal to your level in Cardsharp, then discard down to the appropriate hand-size before each round of play."
    },
    "Careful Strike": {
        "description": "You are skilled at hitting your enemy exactly where you want to, either at range or in melee. You may modify your Hit Location result by up to +/–10 per time you have this Talent. So, if you had this Talent twice and hit location 34, the Right Arm, you could modify this down to 14, the Left Arm, or up to 54, the Body (see page 159)."
    },
    "Carouser": {
        "description": "You are a seasoned drinker and know how to party hard. You may reverse the dice of any failed Consume Alcohol Test if this will score a Success."
    },
    "Catfall": {
        "description": "You are nimble and balanced like a cat, and are able to fall much greater distances unharmed than others might. Whenever you fall, you attempt an Athletics Test. If successful, reduce the distance fallen by 1 yard, +1 extra yard per +1 SL scored, for the purposes of calculating Damage."
    },
    "Cat-tongued": {
        "description": "Like Ranald the Trickster God, you blend truth and lies as if there were no difference. When using Charm to lie, listeners do not get to oppose your Charm with their Intuition to detect if there is something fishy in what you say."
    },
    "Chaos Magic": {
        "description": "Each time you take this Talent, which always costs 100 XP per time instead of the normal cost, you learn another spell from your chosen Lore and gain a Corruption point. For more about the available spells, see Chapter 8: Magic. Under normal circumstances, you may only ever know one Lore of Chaos Magic."
    },
    "Combat Aware": {
        "description": "You are used to scanning the battlefield to make snap decisions informed by the shifting tides of war.You may take a Challenging (+0) Perception Test to ignore Surprise, which is modified by circumstance as normal."
    },
    "Combat Master": {
        "description": "Your accumulated years of combat experience allow you to keep lesser fighters at bay. For each level in this Talent, you count as one more person for the purposes of determining if one side outnumbers the other. This Talent only comes into play when you are out-numbered. See page 162 for the rules for out-numbering."
    },
    "Combat Reflexes": {
        "description": "You react like a flash of lightning. Add 10 to your Initiative for each level in this Talent when determining Combat Initiative."
    },
    "Commanding Presence": {
        "description": "Your presence fills others with hushed awe and admiration. Such is your aura of authority, those with a lower Status may not resist your Leadership tests with their Willpower. Of course, enemies are still no more likely to respect or obey you, but the common folk rarely stand against you."
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
    "Distract": {
        "description": "You are trained in simple movements to distract or startle your opponent, drawing eyes from your true intent. You may use your Move to perform a Distraction. This is resolved by an Opposed Athletics/Cool Test. If you win, your opponent can gain no Advantage until the end of the next Round."
    },
    "Doomed": {
        "description": "At the age of 10, a Priest of Morr called a Doomsayer took you aside to foretell your death in an incense-laden, coming-of-age ritual called the Dooming. In conjunction with your GM, come up with a suitable Dooming. Should your character die in a fashion that matches your Dooming, your next character gains a bonus of half the total XP your dead character accrued during play."
    },
    "Drilled": {
        "description": "You have been trained to fight shoulder-to-shoulder with other soldiers. If an enemy causes you to lose Advantage when standing beside an active ally with the Drilled Talent, you may keep 1 lost Advantage for each time you’ve taken the Drilled Talent."
    },
    "Dual Wielder": {
        "description": "When armed with two weapons, you may attack with both for your Action. Roll to hit with the weapon held in your primary hand. If you hit, determine Damage as normal, but remember to keep your dice roll, as you will use it again. If the first strike hits, once it is resolved, the weapon in your secondary hand can then target an available opponent of your choice using the same dice roll for the first strike, but reversed. So, if you rolled 34 to hit with the first weapon, you use 43 to hit with the second. Remember to modify this second roll by your off-hand penalty (–20 unless you have the Ambidextrous Talent). This second attack is Opposed with a new defending roll, and damage for this second strike is calculated as normal. The only exception to this is if you roll a Critical for your first strike. If this happens, use the roll on the Critical Table to also act as the roll for the second attack. So, if you scored a critical to the head and rolled 56 on the Critical table for a Major Eye Wound, your second attack would then strike out with a to-hit value of 56. If you choose to attack with both weapons, all your defensive rolls until the start of your next Turn suffer a penalty of –10. You do not gain an Advantage when you successfully strike or Wound an opponent when Dual Wielding unless both attacks hit."
    },
    "Embezzle": {
        "description": "You are skilled at skimming money from your employers without being detected. Whenever you secure money when Earning (during play or performing an Income Endeavour), you may attempt an Opposed Intelligence Test with your employer (assuming you have one). If you win, you skim 2d10 + SL brass pennies, 1d10 + SL silver shillings, or 1 + SL gold crowns (depending upon the size of the business in question, as determined by the GM) without being detected. If your employer wins by 6+ SL, you gain the money, but your embezzling is detected; what then happens is left to the GM. Any other result means you have failed to embezzle any money."
    },
    "Enclosed Fighter": {
        "description": "You have learned to make the most benefit out of fighting in enclosed spaces. You ignore penalties to Melee caused by confined spaces such as tunnels, the frontline, small fighting pits, and similar, and can use the Dodge Skill, even if it "
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
    "Fast Hands": {
        "description": "You can move your hands with surprising dexterity. Bystanders get no passive Perception Tests to spot your use of the Sleight of Hand Skill, instead they only get to Oppose your Sleight of Hand Tests if they actively suspect and are looking for your movements. Further, attempts to use Melee (Brawling) to simply touch an opponent gain a bonus of +10 × your level in Fast Hands."
    },
    "Fast Shot": {
        "description": "If you have a loaded ranged weapon, you can fire it outside the normal Initiative Order before any other combatant reacts in the following Round. You roll to hit using all the normal modifiers. Employing Fast Shot requires both your Action and Move for your upcoming turn, and these will count as having been spent when your next turn arrives. If two or more characters use Fast Shot, the character who has taken this Talent most goes first. If any characters have taken Fast Shot an equal number of times, both shots are fired simultaneously, and should both be handled at the same time."
    },
    "Fearless": {
        "description": "You are either brave enough or crazy enough that fear of certain enemies has become a distant memory. With a single Average (+20%) Cool Test, you may ignore any Intimidate, Fear, or Terror effects from the specified enemy when encountered.",
        "specialisations": [
            "Beastmen",
            "Greenskins",
            "Outlaws",
            "Vampires",
            "Watchmen",
            "Witches",
        ],
    },
    "Feint": {
        "description": "You have trained how to make false attacks in close combat to fool your opponent. You may now make a Feint for your Action against any opponent using a weapon. This is resolved with an Opposed Melee (Fencing)/Melee Test. If you win, and you attack the same opponent before the end of the next Round, you may add the SL of your Feint to your attack roll."
    },
    "Field Dressing": {
        "description": "You are used to treating wounds quickly. If you fail a Heal Test when using Bandages, you may reverse the result if this will score a success; however, if you do so, you may not score more than +1 SL as you focus on speed over accuracy."
    },
    "Fisherman": {
        "description": "You are a very capable fisherman and know all the best ways to land fish. Assuming a large enough body of water is available, you are automatically assumed to be able to fish enough to feed yourself and a number of others equal to your level in Fisherman, assuming you choose to spend at least an hour or so with a line and bait. You may secure more fish in addition to this using the normal rules for foraging (see page 127)."
    },
    "Flagellant": {
        "description": "You have dedicated your pain to the service of your God. Each day, you must spend half a bell (half an hour) praying as you maintain a number of Wounds suffered equal to your level in Flagellent. Until you next sleep, if you have the Frenzy Talent you may enter Frenzy immediately without testing."
    },
    "Flee!": {
        "description": "When your life is on the line you are capable of impressive bursts of speed. Your Movement Attribute counts as 1 higher when Fleeing (see page 165)."
    },
    "Fleet Footed": {"description": "You gain +1 to your Movement Attribute."},
    "Frenzy": {"description": "You can Frenzy as described on page 190."},
    "Frightening": {
        "description": "Anyone sane thinks twice before approaching you. If you wish, you have a Fear Rating of 1 (see page 190). Add +1 to this number per extra time you have this Talent."
    },
    "Furious Assault": {
        "description": "Your blows follow one another in quick succession, raining down on your opponents with the fury of Ulric. Once per Round, if you hit an opponent in close combat, you may immediately spend an Advantage or your Move to make an extra attack (assuming you have your Move remaining)."
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
    "Instinctive Diction": {
        "description": "You instinctively understand the language of Magick, and are capable of articulating the most complex phrases rapidly without error. You do not suffer a Miscast if you roll a double on a successful Language (Magick) Test."
    },
    "Invoke": {
        "description": "You are blessed by one of the Gods and can empower one of your Cult’s Miracles. Further, you may purchase extra miracles for 100 XP per miracle you currently know. So, if you already know 3 miracles, your next miracle costs 300 XP to purchase. Full rules for learning new miracles are provided in Chapter 7: Religion and Belief. Under normal circumstances, you may not learn more than one Invoke (Divine Lore) Talent. Further, you may not learn the Petty Magic or Arcane Magic Talents when you have the Invoke Talent. You can unlearn this Talent for 100 XP, but will lose all of your miracles if you do so, and will also garner the extreme disfavour of your God, with effects determined by your GM."
    },
    "Iron Jaw": {
        "description": "You are made of sturdy stuff and can weather even the strongest blows. Whenever you gain one or more Stunned Conditions, you may make an immediate Challenging (+0) Endurance Test to not take one of them, with each SL removing an extra Stunned Condition."
    },
    "Iron Will": {
        "description": "You have an indomitable will of iron, and will never willingly bow down before another. Use of the Intimidate skill does not cause Fear in you, and will not stop you speaking out against the intimidating party."
    },
    "Jump Up": {
        "description": "You are hard to keep down. You may perform a Challenging (+0) Athletics Test to immediately regain your feet whenever you gain a Prone Condition. This Athletics Test is often modified by the Strength behind the blow that knocks you down: for every +10 Strength the blow has over your Toughness, you suffer a penalty of –10 to the Athletics Test, and vice versa."
    },
    "Kingpin": {
        "description": "You have earned an air of respectability despite your nefarious ways. You may ignore the Status loss of the Criminal Talent."
    },
    "Lightning Reflexes": {
        "description": "You gain a permanent +5 bonus to your starting Agility Characteristic (this does not count towards your Advances)."
    },
    "Linguistics": {
        "description": "You have a natural affinity for languages. Given a month’s exposure to any Language, you count the associated Language Skill as a Basic Skill with a successful Intelligence Test (which can be attempted once per month). Note: Linguistics only works for languages used to frequently communicate with others, so does not work with Language (Magick)."
    },
    "Luck": {
        "description": "They say when you were born, Ranald smiled. Your maximum Fortune Points now equal your current Fate points plus the number of times you’ve taken Luck."
    },
    "Magic Resistance": {
        "description": "The SL of any spell affecting you is reduced by 2 per point you have in this Talent."
    },
    "Marksman": {
        "description": "You gain a permanent +5 bonus to your starting Ballistic Skill (this does not count towards your Advances)."
    },
    "Menacing": {
        "description": "You have an imposing presence. When using the Intimidate Skill, gain a SL bonus equal to your levels of Menacing."
    },
    "Mimic": {
        "description": "You have a good ear for accents and dialects, and can reproduce them accurately. You may replicate any accent you are exposed to for at least a day with an Initiative Test; this Test may be attempted once per day. Once passed, you may always mimic the accent, and locals will believe you to be one of their own."
    },
    "Night Vision": {
        "description": "You can see very well in natural darkness. Assuming you have at least a faint source of light (such as starlight, moonlight, or bioluminescence) you can see clearly for 20 yards per level of Night Vision. Further, you can extend the effective illumination distance of any light sources by 20 yards per level of Night Vision."
    },
    "Nimble Fingered": {
        "description": "You gain a permanent +5 bonus to your starting Dexterity (this does not count towards your Advances)."
    },
    "Noble Blood": {
        "description": "You are either born into the nobility, or otherwise elevated to it by in-game events. Assuming you are dressed appropriately, you are always considered of higher Status than others unless they also have the Noble Blood Talent, where Status is compared as normal."
    },
    "Nose for Trouble": {
        "description": "You are used to getting into, and preferably out of, trouble. You may attempt an Intuition Test to spot those seeking to cause trouble or seeking to cause you harm, even if normally you would not be allowed a Test (because of Talents or a Spell, for example). This Test will likely be Opposed if others are hiding, and the GM may prefer to take this Test on your behalf in secret so you do not know the results should you fail. If any troublemakers you spot start combat, you may ignore any Surprised Condition they would normally inflict."
    },
    "Numismatics": {
        "description": "You are well versed with the different coinage of the Old World, and are adept at determining their value. You can judge the true value of a coin by experience alone, not even requiring a Test. Further, you can identify forged coins with a Simple Evaluate Test; it is never Opposed by the SL of the Forger."
    },
    "Old Salt": {
        "description": "You are an experienced seaman, and are very used to sea life. You can ignore all negative modifiers to Tests at sea derived from poor weather, rolling ships, and similar. Further, you count as two seamen towards the minimum number of crew to pilot a sea-going vessel."
    },
    "Orientation": {
        "description": "You are an experienced seaman, and are very used to sea life. You can ignore all negative modifiers to Tests at sea derived from poor weather, rolling ships, and similar. Further, you count as two seamen towards the minimum number of crew to pilot a sea-going vessel."
    },
    "Panhandle": {
        "description": "You are a skilled beggar, able to get even the most jaded individual to contribute to your cause. You can perform a Charm Test every half hour when Begging, not every hour (see page 120)."
    },
    "Perfect Pitch": {
        "description": "You are a skilled beggar, able to get even the most jaded individual to contribute to your cause. You can perform a Charm Test every half hour when Begging, not every hour (see page 120)."
    },
    "Petty Magic": {
        "description": "You have the spark to cast magic within you and have mastered techniques to control it at a basic level. When you take this Talent, you manifest, and permanently memorise, a number of spells equal to your Willpower Bonus."
    },
    "Pharmacist": {
        "description": "You are highly skilled at pharmacy, better able than most to make pills, ointments, unguents, oils, creams, and more. You may reverse any failed Trade (Apothecary) test if this allows the Test to succeed."
    },
    "Pilot": {
        "description": "You are skilled at leading vessels through dangerous waters. If you fail a Test to pass through dangerous waters, you may reverse the result if it will score a success; however, if you do so, you may not score more than +1 SL as you catch the incoming danger at the last moment."
    },
    "Public Speaker": {
        "description": "You are a skilled orator and know how to work large groups of people. Refer to the following table to see how many people you can now influence with your Charm Skill (see page 120) when Public Speaking."
    },
    "Pure Soul": {
        "description": "Your soul is pure, quite resistant to the depredations of Chaos. You may gain extra Corruption points equal to your level of Pure Soul before having to Test to see if you become corrupt."
    },
    "Rapid Reload": {
        "description": "You can reload ranged weapons with practiced ease. You add SL equal to your level in Rapid Reload to any Test to reload a ranged weapon."
    },
    "Reaction Strike": {
        "description": "Your fast reactions have allowed you to fell many opponents before they have even swung their blades. When you are Charged, you may attempt a Challenging (+0) Initiative Test to gain an immediate Free Attack outside the normal turn sequence. This attack is resolved with whatever weapon you are carrying in your primary hand. You may make as many Reaction Strikes in a Round as you have levels in this Talent, but can only attack each individual charger once each."
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
    "Resolute": {
        "description": "You launch into attacks with grim determination. Add your level of Resolute to your Strength Bonus when you Charge."
    },
    "Reversal": {
        "description": "You are used to desperate combats, able to turn even the direst circumstances to your Advantage. If you win an Opposed Melee Test, instead of gaining +1 Advantage, you may take all your opponent’s Current Advantage. If you do this, you do not cause any Damage, even if it is your Turn in the Round."
    },
    "Riposte": {
        "description": "Conforming to ‘the best defence is offence’, you respond to an incoming attack with a lightning-fast counterstrike of your own. If your weapon has the Fast quality, you may cause Damage when you are attacked, just as if it was your Action. You can Riposte a number of attacks per round equal to your Riposte level."
    },
    "River Guide": {
        "description": "You know all the tricks for navigating dangerous rivers. You don’t need to Test for passing through dangerous stretches of water until the Difficulty for doing so is –10 or lower — you automatically pass all Tests easier than this. Further, if you have the appropriate Lore (Local) Skill, you need never Test for navigating dangerous waters — you are assumed to know the route through."
    },
    "Robust": {
        "description": "You are as tough as old boots and just soak up damage. You reduce all incoming Damage by an extra +1 per time you have taken the Robust Talent, even if the Damage cannot normally be reduced, but still suffer a minimum of 1 Wound from any Damage source."
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
    "Scale Sheer Surface": {
        "description": "You are an exceptional climber. You can attempt to climb even seemingly impossible surfaces such as sheer fortifications, ice shelves, plastered walls, and similar, and you ignore any penalties to Climb Tests derived from the difficulty of the surface climbed."
    },
    "Schemer": {
        "description": "You are a master of politics and see conspiracy around every corner. Once per session, you may ask the GM one question regarding a political situation or entangled web of social connections; the GM will perform a secret Intelligence Test and provide you some observations regarding the situation based upon your SL."
    },
    "Sea Legs": {
        "description": "You are used to the rolling motion of the oceans, and are very unlikely to get sea sick, even in the worst storms. Under normal conditions at sea, you need never Test to see if you become Sea Sick. At other times (such as a storm, or a magically induced bout of Sea Sickness), you can ignore any penalties to Tests to avoid Sea Sickness."
    },
    "Seasoned Traveller": {
        "description": "You are an inquisitive soul who has travelled far and wide, learning all manner of local information. Add Lore (Local) to any Career you enter; if it is already in Career, you may purchase the Skill, both times — a different Speciality each time, such as Altdorf, Vorbergland, or Ubersreik — for 5 XP fewer per Advance."
    },
    "Second Sight": {
        "description": "You can perceive the shifting Winds of Magic that course from the Chaos Gates at the poles of the world. You now have the Sight (see page 233)."
    },
    "Secret Identity": {
        "description": "You maintain a secret identity that allows you to appear richer, or perhaps poorer, than you actually are. With GM permission, choose any one Career. As long as you are dressed appropriately, you may use the Social Status of the chosen Career you masquerade as rather than your own for modifying Fellowship Tests, and can even ignore the Criminal Talent. However, maintaining this identity will require Entertain (Acting) rolls when you encounter those who may recognise your falsehood. You may create a new Secret Identity for each level you have in this Talent."
    },
    "Shadow": {
        "description": "You are skilled at following people without being spotted. You may use the Shadowing rules on page 130 without doing a Combined Test. Instead you test against just your Perception or your Stealth Skill, whichever is higher."
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
    "Tinker": {
        "description": "You are somewhat of a Johann-of-all-trades, able to repair almost anything. You count all non-magical Trade Skills as Basic when repairing broken items."
    },
    "Tower of Memories": {
        "description": "A recollection technique first instigated by the Cult of Verena, reputedly from Elven practices taught by the Loremasters of Hoeth, Tower of Memories allows you to perfectly recall a sequence of facts by storing them in an imaginary spire. You can recall a sequence as long as your Intelligence without having to make a Test. For every 10 more items you attempt to memorise, you must make an increasingly difficult Intelligence Test to recall the list correctly, starting at Very Easy (+60) for +10, Easy (+40) for +20, Average (+20) for +30, and so on. Beyond it’s obvious utility for Gamble Tests, where having this Talent adds a bonus of +20 to +60 depending upon how useful recalling sequences is to the game at hand, the GM can apply bonuses to other Tests as appropriate. Each time you take this Talent you may recall an extra sequence without having to forget a previously stored one."
    },
    "Trapper": {
        "description": "You are skilled at spotting and using traps. You may take a Perception Test to spot traps automatically without having to tell the GM of your intention; the GM may prefer to make some of these Tests on your behalf in private."
    },
    "Trick Riding": {
        "description": "You are capable of amazing feats of agility on horseback. You can use any of your Performer Skills and unmodified Dodge skill when on horseback. Further, when mounted, you can make your Move at the start of the Round instead of on your Turn."
    },
    "Tunnel Rat": {
        "description": "You are at home in tunnels, sewers, and other underground environments.When using Stealth in an underground environment, bystanders do not get passive Perception Tests to detect you; they can only spot you if they are specifically on look-out, or watching for hidden others."
    },
    "Unshakable": {
        "description": "You are a jaded veteran who has survived more than one hail of shots from Blackpowder weapons. You need only take a Cool Test to resist a Broken Condition if you are successfully wounded by a Blackpowder weapon, not just if you are shot at."
    },
    "Very Resilient": {
        "description": "You gain a permanent +5 bonus to your starting Toughness Characteristic (this does not count towards your Advances)."
    },
    "Very Strong": {
        "description": "You gain a permanent +5 bonus to your starting Strength Characteristic (this does not count towards your Advances)."
    },
    "War Leader": {
        "description": "Your stern gaze and inspiring words motivate your soldiers to fight on to the end. All subordinates able to see you may add your level in War Leader to their SL in one Willpower Test per Round. This bonus does not stack."
    },
    "War Wizard": {
        "description": "You are trained to cast magic while in the thick of combat. On your Turn, you may cast one Spell with a Casting Number of 5 or less for free without using your Action. However, if you do this, you may not cast another spell this Turn."
    },
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
