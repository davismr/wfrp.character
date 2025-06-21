import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="name", permission="create_character")
class NameViews(BaseView):
    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Character Name")
        schema.add(
            colander.SchemaNode(
                colander.String(),
                title="Character Name",
                validator=colander.Length(max=100),
                widget=deform.widget.TextInputWidget(),
                name="character_name",
            )
        )
        return schema

    @view_config(renderer="wfrp.character:templates/form.pt")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Select Name",))
        if "Select_Name" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                character_name = captured.get("character_name")
                self.character.name = character_name
                url = self.request.route_url(
                    "character_summary", uuid=self.character.uuid
                )
                self.character.status = {"complete": ""}
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
