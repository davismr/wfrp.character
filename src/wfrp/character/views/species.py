from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species")
class SpeciesViews(BaseView):
    def get_species_list(self, item):
        species = ["Human", "Halfling", "Dwarf", "High Elf", "Wood Elf"]
        species.remove(item)
        return species

    def _roll_new_species(self):
        result = roll_d100()
        if result <= 90:
            species = "Human"
        elif result <= 94:
            species = "Halfling"
        elif result <= 98:
            species = "Dwarf"
        elif result == 99:
            species = "High Elf"
        elif result == 100:
            species = "Wood Elf"
        else:
            raise NotImplementedError(f"result {result} does not return a species")
        return species

    @view_config(request_method="GET", renderer=__name__ + ":../templates/species.pt")
    def new_species_view(self):
        if self.character.status["species"]:
            species = self.character.status["species"]
        else:
            species = self._roll_new_species()
            self.character.status = {"species": species}
        return {"species": species, "species_list": self.get_species_list(species)}

    def _set_species_attributes(self, species):
        if species == "Human":
            self.character.fate = 2
            self.character.resilience = 1
            self.character.extra_points = 3
            self.character.movement = 4
        elif species == "Halfling":
            self.character.resilience = 2
            self.character.extra_points = 2
        elif species == "Dwarf":
            self.character.resilience = 2
            self.character.extra_points = 3
        elif species in ["High Elf", "Wood Elf"]:
            self.character.extra_points = 2
            self.character.movement = 5
        else:
            raise NotImplementedError(f"{species} is not defined")

    @view_config(request_method="POST")
    def submit_species_view(self):
        species = self.request.POST.get("species")
        if species == self.character.status["species"]:
            self.character.experience += 20
        self.character.species = species
        self._set_species_attributes(species)
        url = self.request.route_url("career", uuid=self.character.uuid)
        self.character.status = {"career": ""}
        return HTTPFound(location=url)
