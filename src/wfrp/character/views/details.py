import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.species import get_eye_colour
from wfrp.character.data.species import get_hair_colour
from wfrp.character.utils import roll_2d10
from wfrp.character.utils import roll_5d10
from wfrp.character.utils import roll_d10
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="details")
class DetailsViews(BaseView):
    def _get_hair_colour(self, species):
        return get_hair_colour(species, roll_2d10())

    def _get_eye_colour(self, species):
        return get_eye_colour(species, roll_2d10())

    def initialise_form(self):
        if self.character.status["details"]:
            return self.character.status["details"]
        species = self.character.species
        eye_colour = ""
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
            eye_colour += f"{self._get_eye_colour(species)}, "
        else:
            raise NotImplementedError(f"{species} is not defined")
        # eye colour is set here to allow previous catch to raise the error
        eye_colour += self._get_eye_colour(species)
        data = {
            "age": age,
            "height": height,
            "hair_colour": self._get_hair_colour(species),
            "eye_colour": eye_colour,
        }
        self.character.status = {"details": data}
        return data

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(), title=self.character.get_display_title()
        )
        details_schema = colander.SchemaNode(
            colander.Mapping(),
            name="character_details",
        )
        details_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                missing="",
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

    @view_config(renderer="wfrp.character:templates/details.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema, buttons=("Choose Details",), appstruct={"character_details": data}
        )
        if "Choose_Details" in self.request.POST:
            try:
                form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.character.eyes = self.character.status["details"]["eye_colour"]
                self.character.hair = self.character.status["details"]["hair_colour"]
                self.character.height = self.character.status["details"]["height"]
                self.character.age = self.character.status["details"]["age"]
                url = self.request.route_url("name", uuid=self.character.uuid)
                self.character.status = {"name": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
