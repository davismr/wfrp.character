import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.expansions import EXPANSIONS
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(route_name="expansions", permission="create_character")
class ExpansionsViews(BaseCreateView):
    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Enabled Expansions")
        expansions_schema = colander.SchemaNode(
            colander.Mapping(),
            name="expansions",
        )
        choices = [
            (expansion[0], expansion[1]["title"]) for expansion in EXPANSIONS.items()
        ]
        expansions_schema.add(
            colander.SchemaNode(
                colander.Set(),
                name="expansions",
                widget=deform.widget.CheckboxChoiceWidget(values=choices),
                allow_empty=True,
                validator=colander.ContainsOnly(EXPANSIONS.keys()),
                missing=[],
            )
        )
        schema.add(expansions_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/forms/base_form.pt")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(
            schema,
            buttons=("Choose Expansions",),
        )
        if "Choose_Expansions" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.character.expansions = list(captured["expansions"]["expansions"])
                url = self.request.route_url("species", id=self.character.id)
                self.character.status = {"species": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
