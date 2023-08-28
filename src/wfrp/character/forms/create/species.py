import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species")
class SpeciesViews(BaseView):
    def _get_species_list(self):
        return (
            ("Human", "Human"),
            ("Halfling", "Halfling"),
            ("Dwarf", "Dwarf"),
            ("High Elf", "High Elf"),
            ("Wood Elf", "Wood Elf"),
        )

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

    def initialise_form(self):
        if self.character.status["species"]:
            species = self.character.status["species"]
        else:
            species = self._roll_new_species()
            self.character.status = {"species": species}
        species_list = self._get_species_list()
        return species_list

    def schema(self, data):
        species = self.character.status["species"]
        schema = colander.SchemaNode(colander.Mapping(), title="Character Species")
        species_schema = colander.SchemaNode(
            colander.Mapping(),
            name="species",
        )
        species_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="species",
                default=species,
                validator=colander.OneOf([x[0] for x in data]),
                widget=deform.widget.RadioChoiceWidget(values=data),
                description=f"Select {species} for 20XP or select another species",
            )
        )
        schema.add(species_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/form.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(schema, buttons=("Choose Species",))

        if "Choose_Species" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                selected = captured["species"]["species"]
                if selected == self.character.status["species"]:
                    self.character.experience += 20
                self.character.species = selected
                self._set_species_attributes(selected)
                url = self.request.route_url("career", uuid=self.character.uuid)
                self.character.status = {"career": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

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
