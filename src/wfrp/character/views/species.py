from pyramid.renderers import render
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.response import Response

from wfrp.character.utils import roll_d100


@view_defaults(route_name="species")
class SpeciesViews:
    def __init__(self, request):
        self.request = request

    def get_species_list(request):
        return ["Human", "Halfling", "Dwarf", "High Elf", "Wood Elf"]

    @view_config(request_method="GET")
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
        import pdb;pdb.set_trace()
        result = render(
            "wfrp.character:../templates/homepage.pt", {"result": result, "species_list": self.get_species_list()}, request=self.request
        )
        return Response(result)
