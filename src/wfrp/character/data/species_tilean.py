from wfrp.character.data.species_standard import STANDARD_SPECIES_DATA

TILEAN_SPECIES_DATA = {
    "Human (Tilean)": {
        "skills": [
            "Charm",
            "Cool",
            "Evaluate",
            "Gossip",
            "Haggle",
            "Language (Arabyan)",
            "Language (Estalian)",
            "Language (Reikspiel)",
            "Lore (Tilea)",
            "Melee (Basic)",
            "Ranged (Crossbow)",
            "Sail",
        ],
        "talents": [
            "Argumentative or Fisherman",
            "Coolheaded or Suave",
        ],
        # 3 Random Talents
        "hair_colour": STANDARD_SPECIES_DATA["Human"]["hair_colour"].copy(),
        "eye_colour": STANDARD_SPECIES_DATA["Human"]["eye_colour"].copy(),
    },
}

# TODO: Characters from Luccini may at their option replace one
# of their starting Talents with Doomed
