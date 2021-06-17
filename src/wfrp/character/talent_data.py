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
    "Acute Sense (any one)": {
        "description": "You are an exceptional shot and know where to shoot an enemy in order to inflict maximum damage. You deal your Accurate Shot level in extra Damage with all ranged weapons."
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
    "Blather": {
        "description": "Attempt an Opposed Charm/Intelligence Test. Success gives your opponent a Stunned Condition. Further, for each level you have in Blather, your opponent gains another Stunned Condition. Targets Stunned by Blather may do nothing other than stare at you dumbfounded as they try to catch-up with or understand what you are saying. "
    },
    "Coolheaded": {"description": ""},
    "Craftsman (any one)": {"description": ""},
    "Disarm": {
        "description": "You are able to disarm an opponent with a careful flick of the wrist or a well-aimed blow to the hand."
    },
    "Doomed": {
        "description": "At the age of 10, a Priest of Morr called a Doomsayer took you aside to foretell your death in an incense-laden, coming-of-age ritual called the Dooming. In conjunction with your GM, come up with a suitable Dooming. Should your character die in a fashion that matches your Dooming, your next character gains a bonus of half the total XP your dead character accrued during play."
    },
    "Flee!": {"description": ""},
    "Hardy": {"description": ""},
    "Lightning Reflexes": {"description": ""},
    "Linguistics": {"description": ""},
    "Luck": {"description": ""},
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
    "Read/Write": {"description": ""},
    "Resistance (any one)": {
        "description": "Your strong constitution allows you to more readily survive a specific threat. You may automatically pass the first Test to resist the specified threat, such as Magic, Poison, Disease, Mutation, every session. If SL is important, use your Toughness Bonus as SL for the Test."
    },
    "Savvy": {
        "description": "You gain a permanent +5 bonus to your starting Intelligence Characteristic (this does not count towards your Advances)"
    },
    "Sharp": {"description": ""},
    "Sixth Sense": {"description": ""},
    "Strong Legs": {"description": ""},
    "Sturdy": {"description": ""},
    "Suave": {"description": ""},
    "Super Numerate": {"description": ""},
    "Very Resilient": {"description": ""},
    "Very Strong": {"description": ""},
    "Warrior Born": {"description": ""},
}
