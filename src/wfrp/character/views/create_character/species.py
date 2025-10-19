import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.species import get_species_list
from wfrp.character.utils import roll_d100
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class SpeciesViews(BaseCreateView):
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

    def _roll_new_species_with_gnome(self):
        result = roll_d100()
        if result <= 89:
            species = "Human"
        elif result <= 93:
            species = "Halfling"
        elif result <= 97:
            species = "Dwarf"
        elif result == 98:
            species = "Gnome"
        elif result == 99:
            species = "High Elf"
        elif result == 100:
            species = "Wood Elf"
        else:
            raise NotImplementedError(f"result {result} does not return a species")
        return species

    def initialise_form(self):
        self.species_list = get_species_list(self.character.expansions)
        if not self.character.create_data["species"]:
            if "rough_nights" in self.character.expansions:
                species = self._roll_new_species_with_gnome()
            else:
                species = self._roll_new_species()
            self.character.create_data = {"species": species}

    def schema(self):
        species = self.character.create_data["species"]
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
                validator=colander.OneOf(self.species_list),
                widget=deform.widget.RadioChoiceWidget(
                    values=[(x, x) for x in self.species_list]
                ),
                description=f"Select {species} for 20XP or select another species",
            )
        )
        schema.add(species_schema)
        return schema

    @view_config(route_name="species")
    def form_view(self):
        self.initialise_form()
        schema = self.schema()
        form = deform.Form(schema, buttons=("Choose Species",))
        if "Choose_Species" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                selected = captured["species"]["species"]
                if selected == self.character.create_data["species"]:
                    self.character.experience += 20
                self.character.species = selected
                self._set_species_attributes(selected)
                url = self.request.route_url("career", id=self.character.id)
                self.character.create_data = {"career": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    def _set_species_attributes(self, species):
        if species.startswith("Human"):
            self.character.fate = 2
            self.character.resilience = 1
            self.character.extra_points = 3
            self.character.movement = 4
        elif species == "Halfling":
            self.character.resilience = 2
            self.character.extra_points = 2
        elif species in ["Dwarf", "Dwarf (Norse)"]:
            self.character.resilience = 2
            self.character.extra_points = 3
        elif species == "Gnome":
            self.character.fate = 2
            self.character.resilience = 0
            self.character.extra_points = 2
        elif species in ["High Elf", "Wood Elf"]:
            self.character.extra_points = 2
            self.character.movement = 5
        else:
            raise NotImplementedError(f"{species} is not defined")
