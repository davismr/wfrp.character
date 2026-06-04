import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.religions import RELIGION_DATA
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class ReligionViews(BaseCreateView):
    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Character Religion")
        religion_schema = colander.SchemaNode(
            colander.Mapping(),
            name="religion",
        )
        choices = [("None", "No religion")]
        for religion in RELIGION_DATA:
            choices.append((religion, religion))
        religion_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="religion",
                validator=self.validate_religion,
                widget=deform.widget.RadioChoiceWidget(values=choices),
                default="None",
            )
        )
        schema.add(religion_schema)
        return schema

    def validate_religion(self, node, value):
        if self.character.career in ["Nun", "Priest", "Warrior Priest"]:
            if value == "None":
                raise colander.Invalid(
                    node, f"A {self.character.career} has to select a religion"
                )

    @view_config(route_name="religion")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=["Choose Religion"])
        if "Choose_Religion" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                religion = captured["religion"]["religion"]
                if religion != "None":
                    self.character.religion = religion
                url = self.request.route_url("attributes", id=self.character.id)
                self.character.create_data = {"attributes": ""}
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
