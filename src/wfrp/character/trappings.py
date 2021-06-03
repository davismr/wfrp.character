from wfrp.character.utils import roll_d10

# TODO these will randomise on startup
CLASS_TRAPPINGS = {
    "Academics": [
        "Clothing",
        "Dagger",
        "Pouch",
        "Sling Bag",
        "Writing Kit",
        f"{roll_d10()} sheets of Parchment",
    ],
    "Burghers": ["Cloak", "Clothing", "Dagger", "Hat", "Pouch", "Sling Bag", "Lunch"],
    "Courtiers": ["Dagger", "Fine Clothing", "Pouch", "Tweezers", "Ear Pick", "Comb"],
    "Peasants": [
        "Cloak",
        "Clothing",
        "Dagger",
        "Pouch",
        "Sling Bag",
        "Rations (1 day)",
    ],
    "Rangers": [
        "Cloak",
        "Clothing",
        "Dagger",
        "Pouch",
        "Backpack",
        "Tinderbox",
        "Blanket",
        "Rations (1 day)",
    ],
    "Riverfolk": [
        "Cloak",
        "Clothing",
        "Dagger",
        "Pouch",
        "Sling Bag",
        "Flask of Spirits",
    ],
    "Rogues": [
        "Clothing",
        "Dagger",
        "Pouch",
        "Sling Bag",
        "2 Candles",
        f"{roll_d10()} Matches",
        "Hood or Mask",
    ],
    "Warriors": ["Clothing", "Hand Weapon", "Dagger", "Pouch"],
}
