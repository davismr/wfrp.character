from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.utils import roll_2d10
from wfrp.character.utils import roll_5d10
from wfrp.character.utils import roll_d10
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="details")
class DetailsViews(BaseView):
    def _get_hair_colour(self, species):
        result = roll_2d10()
        if species == "Human":
            if result == 2:
                hair_colour = "White Blond"
            elif result == 3:
                hair_colour = "Golden Blond"
            elif result == 4:
                hair_colour = "Red Blond"
            elif result in [5, 6, 7]:
                hair_colour = "Golden Brown"
            elif result in [8, 9, 10, 11]:
                hair_colour = "Light Brown"
            elif result in [12, 13, 14]:
                hair_colour = "Dark Brown"
            elif result in [15, 16, 17]:
                hair_colour = "Black"
            elif result == 18:
                hair_colour = "Auburn"
            elif result == 19:
                hair_colour = "Red"
            elif result == 20:
                hair_colour = "Grey"
        elif species == "Halfling":
            if result == 2:
                hair_colour = "Grey"
            elif result == 3:
                hair_colour = "Flaxen"
            elif result == 4:
                hair_colour = "Russet"
            elif result in [5, 6, 7]:
                hair_colour = "Honey"
            elif result in [8, 9, 10, 11]:
                hair_colour = "Chestnut"
            elif result in [12, 13, 14]:
                hair_colour = "Ginger"
            elif result in [15, 16, 17]:
                hair_colour = "Mustard"
            elif result == 18:
                hair_colour = "Almond"
            elif result == 19:
                hair_colour = "Chocolate"
            elif result == 20:
                hair_colour = "Liquorice"
        elif species == "Dwarf":
            if result == 2:
                hair_colour = "White"
            elif result == 3:
                hair_colour = "Grey"
            elif result == 4:
                hair_colour = "Pale Blond"
            elif result in [5, 6, 7]:
                hair_colour = "Golden"
            elif result in [8, 9, 10, 11]:
                hair_colour = "Copper"
            elif result in [12, 13, 14]:
                hair_colour = "Bronze"
            elif result in [15, 16, 17]:
                hair_colour = "Brown"
            elif result == 18:
                hair_colour = "Dark Brown"
            elif result == 19:
                hair_colour = "Reddish Brown"
            elif result == 20:
                hair_colour = "Black"
        elif species == "High Elf":
            if result == 2:
                hair_colour = "Silver"
            elif result == 3:
                hair_colour = "White"
            elif result == 4:
                hair_colour = "Pale Blond"
            elif result in [5, 6, 7]:
                hair_colour = "Blond"
            elif result in [8, 9, 10, 11]:
                hair_colour = "Yellow Blond"
            elif result in [12, 13, 14]:
                hair_colour = "Copper Blond"
            elif result in [15, 16, 17]:
                hair_colour = "Red Blond"
            elif result == 18:
                hair_colour = "Auburn"
            elif result == 19:
                hair_colour = "Red"
            elif result == 20:
                hair_colour = "Black"
        elif species == "Wood Elf":
            if result == 2:
                hair_colour = "Birch Silver"
            elif result == 3:
                hair_colour = "Ash Blond"
            elif result == 4:
                hair_colour = "Rose Gold"
            elif result in [5, 6, 7]:
                hair_colour = "Honey Blond"
            elif result in [8, 9, 10, 11]:
                hair_colour = "Brown"
            elif result in [12, 13, 14]:
                hair_colour = "Mahogany Brown"
            elif result in [15, 16, 17]:
                hair_colour = "Dark Brown"
            elif result == 18:
                hair_colour = "Sienna"
            elif result == 19:
                hair_colour = "Ebony"
            elif result == 20:
                hair_colour = "Blue-Black"
        return hair_colour

    def _get_eye_colour(self, species):
        result = roll_2d10()
        if species == "Human":
            if result == 2:
                eye_colour = ""
            elif result == 3:
                eye_colour = "Green"
            elif result == 4:
                eye_colour = "Pale Blue"
            elif result in [5, 6, 7]:
                eye_colour = "Blue"
            elif result in [8, 9, 10, 11]:
                eye_colour = "Pale Grey"
            elif result in [12, 13, 14]:
                eye_colour = "Grey"
            elif result in [15, 16, 17]:
                eye_colour = "Brown"
            elif result == 18:
                eye_colour = "Hazel"
            elif result == 19:
                eye_colour = "Dark Brown"
            elif result == 20:
                eye_colour = "Black"
        elif species == "Halfling":
            if result == 2:
                eye_colour = "Light Grey"
            elif result == 3:
                eye_colour = "Grey"
            elif result == 4:
                eye_colour = "Pale Blue"
            elif result in [5, 6, 7]:
                eye_colour = "Blue"
            elif result in [8, 9, 10, 11]:
                eye_colour = "Green"
            elif result in [12, 13, 14]:
                eye_colour = "Hazel"
            elif result in [15, 16, 17]:
                eye_colour = "Brown"
            elif result == 18:
                eye_colour = "Copper"
            elif result in [19, 20]:
                eye_colour = "Dark Brown"
        elif species == "Dwarf":
            if result == 2:
                eye_colour = "Coal"
            elif result == 3:
                eye_colour = "Lead"
            elif result == 4:
                eye_colour = "Steel"
            elif result in [5, 6, 7]:
                eye_colour = "Blue"
            elif result in [8, 9, 10, 11]:
                eye_colour = "Earth Brown"
            elif result in [12, 13, 14]:
                eye_colour = "Dark Brown"
            elif result in [15, 16, 17]:
                eye_colour = "Hazel"
            elif result == 18:
                eye_colour = "Green"
            elif result == 19:
                eye_colour = "Copper"
            elif result == 20:
                eye_colour = "Gold"
        elif species == "High Elf":
            if result == 2:
                eye_colour = "Jet"
            elif result == 3:
                eye_colour = "Amethyst"
            elif result == 4:
                eye_colour = "Aquamarine"
            elif result in [5, 6, 7]:
                eye_colour = "Sapphire"
            elif result in [8, 9, 10, 11]:
                eye_colour = "Turquoise"
            elif result in [12, 13, 14]:
                eye_colour = "Emerald"
            elif result in [15, 16, 17]:
                eye_colour = "Amber"
            elif result == 18:
                eye_colour = "Copper"
            elif result == 19:
                eye_colour = "Citrine"
            elif result == 20:
                eye_colour = "Gold"
        elif species == "Wood Elf":
            if result == 2:
                eye_colour = "Ivory"
            elif result == 3:
                eye_colour = "Charcoal"
            elif result == 4:
                eye_colour = "Ivy Green"
            elif result in [5, 6, 7]:
                eye_colour = "Mossy Green"
            elif result in [8, 9, 10, 11, 12, 13, 14]:
                eye_colour = "Chestnut"
            elif result in [15, 16, 17]:
                eye_colour = "Dark Brown"
            elif result == 18:
                eye_colour = "Tan"
            elif result == 19:
                eye_colour = "Sandy Brown"
            elif result == 20:
                eye_colour = "Violet"
        else:
            raise NotImplementedError(f"{species} is not defined")
        return eye_colour

    @view_config(request_method="GET", renderer=__name__ + ":../templates/details.pt")
    def get_view(self):
        species = self.character.species
        eye_colour = self._get_eye_colour(species)
        if species == "Human":
            age = 15 + roll_d10()
            height = 57 + roll_2d10()
        elif species == "Halfling":
            age = 15 + roll_5d10()
            height = 37 + roll_d10()
        elif species == "Dwarf":
            age = 15 + roll_5d10() + roll_5d10()
            height = 51 + roll_d10()
        elif species in ["High Elf", "Wood Elf"]:
            age = 30 + roll_5d10() + roll_5d10()
            height = 71 + roll_d10()
            eye_colour += f", {self._get_eye_colour(species)}"
        else:
            raise NotImplementedError(f"{species} is not defined")
        return {
            "age": age,
            "height": height,
            "hair_colour": self._get_hair_colour(species),
            "eye_colour": eye_colour,
        }

    @view_config(request_method="POST", renderer=__name__ + ":../templates/details.pt")
    def submit_view(self):
        url = self.request.route_url("name", uuid=self.character.uuid)
        self.character.status = {"name": ""}
        return HTTPFound(location=url)
