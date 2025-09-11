import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.expansions import EXPANSIONS
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class ExpansionsViews(BaseCreateView):
    def initialise_form(self):
        if self.character.campaign:
            self.available_expansions = self.character.campaign.expansions
            self.restricted_expansions = True
        # TODO: also check user and application settings
        else:
            self.available_expansions = list(EXPANSIONS.keys())
            self.restricted_expansions = False

    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Enabled Expansions")
        expansions_schema = colander.SchemaNode(
            colander.Mapping(),
            name="expansions",
        )
        choices = (("false", "Not Enabled"), ("true", "Enabled"))
        for expansion in self.available_expansions:
            read_only = False
            if self.restricted_expansions and expansion in [
                "rough_nights",
                "up_in_arms",
            ]:
                read_only = True
            expansions_schema.add(
                colander.SchemaNode(
                    colander.Boolean(),
                    name=expansion,
                    title=EXPANSIONS[expansion]["title"],
                    description=EXPANSIONS[expansion]["description"],
                    widget=deform.widget.RadioChoiceWidget(
                        values=choices, readonly=read_only
                    ),
                    label="Enabled",
                    default=self.restricted_expansions,
                    missing=self.restricted_expansions,
                )
            )
        schema.add(expansions_schema)
        return schema

    @view_config(route_name="expansions")
    def form_view(self):
        self.initialise_form()
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
                enabled_expansions = []
                for expansion in captured["expansions"]:
                    if captured["expansions"][expansion]:
                        enabled_expansions.append(expansion)
                self.character.expansions = enabled_expansions
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
