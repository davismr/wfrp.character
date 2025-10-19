import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.species import SPECIES_DATA
from wfrp.character.data.species import get_eye_colour
from wfrp.character.data.species import get_hair_colour
from wfrp.character.utils import roll_2d10
from wfrp.character.utils import roll_5d10
from wfrp.character.utils import roll_d10
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class DetailsViews(BaseCreateView):
    def _get_hair_colour(self, species):
        return get_hair_colour(species, roll_2d10())

    def _get_eye_colour(self, species):
        return get_eye_colour(species, roll_2d10())

    def initialise_form(self):
        if self.character.create_data["details"]:
            return self.character.create_data["details"]
        species = self.character.species
        eye_colour = ""
        if species.startswith("Human"):
            age = 15 + roll_d10()
            height = 57 + roll_2d10()
        elif species == "Halfling":
            age = 15 + roll_5d10()
            height = 37 + roll_d10()
        elif species in ["Dwarf", "Dwarf (Norse)"]:
            age = 15 + roll_5d10() + roll_5d10()
            height = 51 + roll_d10()
        elif species == "Gnome":
            age = 20 + roll_5d10() + roll_5d10()
            height = 40 + roll_d10()
        elif species in ["High Elf", "Wood Elf"]:
            age = 30 + roll_5d10() + roll_5d10()
            height = 71 + roll_d10()
        else:
            raise NotImplementedError(f"{species} is not defined")
        eye_colour += self._get_eye_colour(species)
        if species in ["High Elf", "Wood Elf"]:
            second_eye_colour = self._get_eye_colour(species)
            if second_eye_colour != eye_colour:
                eye_colour += f" and {second_eye_colour}"
        data = {
            "age": age,
            "height": height,
            "hair_colour": self._get_hair_colour(species),
            "eye_colour": eye_colour,
        }
        self.character.create_data = {"details": data}
        return data

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(), title=self.character.get_display_title()
        )
        details_schema = colander.SchemaNode(
            colander.Mapping(),
            name="character_details",
        )
        if data["eye_colour"]:
            details_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    widget=deform.widget.TextInputWidget(readonly=True),
                    missing="",
                    name="eye_colour",
                )
            )
        else:
            eye_colours = SPECIES_DATA["Human"]["eye_colour"].values()
            details_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    widget=deform.widget.RadioChoiceWidget(
                        values=[(i, i) for i in eye_colours if i], inline=True
                    ),
                    name="eye_colour",
                )
            )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                missing="",
                name="hair_colour",
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                missing="",
                name="height",
            )
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                missing=data["age"],
                name="age",
            )
        )
        schema.add(details_schema)
        return schema

    @view_config(route_name="details")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema, buttons=("Choose Details",), appstruct={"character_details": data}
        )
        if "Choose_Details" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if self.character.create_data["details"]["eye_colour"]:
                    self.character.eyes = self.character.create_data["details"][
                        "eye_colour"
                    ]
                else:
                    self.character.eyes = captured["character_details"]["eye_colour"]
                self.character.hair = self.character.create_data["details"][
                    "hair_colour"
                ]
                self.character.height = self.character.create_data["details"]["height"]
                self.character.age = self.character.create_data["details"]["age"]
                url = self.request.route_url("name", id=self.character.id)
                self.character.create_data = {"name": ""}
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
