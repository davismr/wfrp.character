CAREERS = [
    # Academics
    "Apothecary",
    "Engineer",
    "Lawyer",
    "Nun",
    "Physician",
    "Priest",
    "Scholar",
    "Wizard",
    # Burghers
    "Agitator",
    "Artisan",
    "Beggar",
    "Investigator",
    "Merchant",
    "Rat Catcher",
    "Townsman",
    "Watchman",
    # Courtiers
    "Advisor",
    "Artist",
    "Duellist",
    "Envoy",
    "Noble",
    "Servant",
    "Spy",
    "Warden",
    # Peasants
    "Bailiff",
    "Hedge Witch",
    "Herbalist",
    "Hunter",
    "Miner",
    "Mystic",
    "Scout",
    "Villager",
    # Rangers
    "Bounty Hunter",
    "Coachman",
    "Entertainer",
    "Flagellant",
    "Messenger",
    "Pedlar",
    "Road Warden",
    "Witch Hunter",
    # Riverfolk
    "Boatman",
    "Huffer",
    "Riverwarden",
    "Riverwoman",
    "Seaman",
    "Smuggler",
    "Stevedore",
    "Wrecker",
    # Rogues
    "Bawd",
    "Charlatan",
    "Fence",
    "Grave Robber",
    "Outlaw",
    "Racketeer",
    "Thief",
    "Witch",
    # Warriors
    "Cavalryman",
    "Guard",
    "Knight",
    "Pit Fighter",
    "Protagonist",
    "Soldier",
    "Slayer",
    "Warrior Priest",
]

WOOD_ELF_CAREERS = {
    1: "Scholar",
    5: "Wizard",
    10: "Artisan",
    14: "Advisor",
    18: "Artist",
    25: "Envoy",
    31: "Noble",
    35: "Spy",
    42: "Herbalist",
    52: "Hunter",
    57: "Mystic",
    68: "Scout",
    70: "Bounty Hunter",
    75: "Entertainer",
    78: "Messenger",
    79: "Wrecker",
    85: "Outlaw",
    90: "Cavalryman",
    92: "Guard",
    94: "Knight",
    96: "Pit Fighter",
    100: "Soldier",
}


def list_careers(species=None):
    if species is None:
        return CAREERS
    if species == "Human":
        return CAREERS.pop("Slayer")
    elif species == "Halfling":
        return
    elif species == "Dwarf":
        return
    elif species == "High Elf":
        return
    elif species == "Wood Elf":
        return list(WOOD_ELF_CAREERS.values())
    raise NotImplementedError("Invalid species sent to list careers")


def get_career(species, die_roll):
    if species == "Wood Elf":
        while True:
            try:
                return WOOD_ELF_CAREERS[die_roll]
            except KeyError:
                die_roll += 1
