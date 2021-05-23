from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.utils import roll_d100


@view_defaults(route_name="species")
class SpeciesViews:
    def __init__(self, request):
        self.request = request

    def get_species_list(self, item):
        species = ["Human", "Halfling", "Dwarf", "High Elf", "Wood Elf"]
        species.remove(item)
        return species

    @view_config(request_method="GET", renderer=__name__ + ":../templates/species.pt")
    def new_species_view(self):
        result = roll_d100()
        if result <= 90:
            result = "Human"
        elif result <= 94:
            result = "Halfling"
        elif result <= 98:
            result = "Dwarf"
        elif result == 99:
            result = "High Elf"
        elif result == 100:
            result = "Wood Elf"
        else:
            raise NotImplementedError(f"result {result} does not return a species")
        return {"result": result, "species_list": self.get_species_list(result)}

    @view_config(request_method="POST")
    def submit_species_view(self):
        uuid = self.request.matchdict["uuid"]
        character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        species = self.request.POST.get("species")
        if "+" in species:
            species = species[:-1]
            character.experience += 20
        character.species = species
        url = self.request.route_url("homepage")
        return HTTPFound(location=url)
