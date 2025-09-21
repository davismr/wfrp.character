import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class NameViews(BaseCreateView):
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
        motivation_schema = colander.SchemaNode(
            colander.Mapping(),
            name="motivation",
            description=(
                "Enter a motivation. You will not be able to change this later."
            ),
        )
        motivation_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="motivation",
                description=(
                    "Enter a motivation for your character. This should be a word or "
                    "short phrase that sums up what your character lives for.\n"
                    "When considering your Motivation, think of something that is "
                    "fundamental to your character’s nature. Also try to make your "
                    "Motivation something fun to roleplay, and something that will "
                    "work well with the other PCs and their motivations"
                ),
                validator=colander.Length(max=100),
                widget=deform.widget.TextInputWidget(),
                default=self.character.motivation or "",
                missing="",
            )
        )
        schema.add(motivation_schema)
        ambition_schema = colander.SchemaNode(
            colander.Mapping(),
            name="ambition",
            description=(
                "Ambitions are a Character’s goals in life – what they want to "
                "achieve. All characters have both a Short-Term and Long-Term "
                "Ambition. You can change ambitions between sessions."
            ),
        )
        ambition_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="short_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.short_term_ambition or "",
                missing="",
            )
        )
        ambition_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="long_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.long_term_ambition or "",
                missing="",
            )
        )
        schema.add(ambition_schema)
        return schema

    @view_config(route_name="name")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Select Name",))
        if "Select_Name" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.character.name = captured.get("character_name")
                self.character.motivation = captured["motivation"]["motivation"]
                self.character.short_term_ambition = captured["ambition"][
                    "short_term_ambition"
                ]
                self.character.long_term_ambition = captured["ambition"][
                    "long_term_ambition"
                ]
                url = self.request.route_url("character-summary", id=self.character.id)
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
