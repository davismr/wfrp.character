import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.magic.petty import PETTY_MAGIC_DATA
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class SpellsViews(BaseCreateView):
    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Spells")
        spells_schema = colander.SchemaNode(
            colander.Mapping(),
            name="spells",
            validator=self.validate_spells,
            description=f"Select {self.character.willpower // 10} spells",
        )
        for spell in PETTY_MAGIC_DATA:
            spells_schema.add(
                colander.SchemaNode(
                    colander.Boolean(),
                    widget=deform.widget.CheckboxWidget(),
                    name=spell,
                    label=spell,
                    description=PETTY_MAGIC_DATA[spell]["description"],
                    missing=False,
                )
            )
        schema.add(spells_schema)
        return schema

    def validate_spells(self, node, values):
        number_spells = self.character.willpower // 10
        spells = [spell for spell, selected in values.items() if selected]
        if len(spells) > number_spells:
            error_msg = f"You can only select {number_spells} spells"
            error = colander.Invalid(node, error_msg)
            for spell in values:
                if values[spell] is True:
                    error[spell] = error_msg
            raise error
        if len(spells) < number_spells:
            error_msg = f"You have to select {number_spells} spells"
            error = colander.Invalid(node, error_msg)
            for spell in values:
                if values[spell] is False:
                    error[spell] = error_msg
            raise error

    @view_config(route_name="spells")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Choose Spells",))
        if "Choose_Spells" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                petty_spells = [
                    spell for spell, selected in captured["spells"].items() if selected
                ]
                self.character.petty_magic = petty_spells
                self.character.create_data = {"trappings": ""}
                url = self.request.route_url("trappings", id=self.character.id)
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
