from wfrp.character.utils import roll_d10


def get_class_trappings(career_class):
    if career_class == "Academics":
        trappings = [
            "Clothing",
            "Dagger",
            "Pouch",
            "Sling Bag",
            "Writing Kit",
            f"{roll_d10()} sheets of Parchment",
        ]
    elif career_class == "Burghers":
        trappings = [
            "Cloak",
            "Clothing",
            "Dagger",
            "Hat",
            "Pouch",
            "Sling Bag",
            "Lunch",
        ]
    elif career_class == "Courtiers":
        trappings = ["Dagger", "Fine Clothing", "Pouch", "Tweezers", "Ear Pick", "Comb"]
    elif career_class == "Peasants":
        trappings = [
            "Cloak",
            "Clothing",
            "Dagger",
            "Pouch",
            "Sling Bag",
            "Rations, 1 day",
        ]
    elif career_class == "Rangers":
        trappings = [
            "Cloak",
            "Clothing",
            "Dagger",
            "Pouch",
            "Backpack",
            "Tinderbox",
            "Blanket",
            "Rations, 1 day",
        ]
    elif career_class == "Riverfolk":
        trappings = [
            "Cloak",
            "Clothing",
            "Dagger",
            "Pouch",
            "Sling Bag",
            "Flask of Spirits",
        ]
    elif career_class == "Seafarer":
        trappings = [
            "Cloak",
            "Clothing",
            "Dagger",
            "Pouch",
            "Sling Bag",
            "Rope, 10 yards",
            "Flask of Spirits",
        ]
    elif career_class == "Rogues":
        trappings = [
            "Clothing",
            "Dagger",
            "Pouch",
            "Sling Bag",
            "2 Candles",
            f"{roll_d10()} Matches",
            "Hood or Mask",
        ]
    elif career_class == "Warriors":
        trappings = ["Clothing", "Hand Weapon", "Dagger", "Pouch"]
    else:
        raise NotImplementedError("Career class not defined")
    return trappings
