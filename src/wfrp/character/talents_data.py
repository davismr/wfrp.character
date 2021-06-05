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


def get_random_talent(die_roll):
    while True:
        try:
            return TALENT_LIST[die_roll]
        except KeyError:
            die_roll += 1
