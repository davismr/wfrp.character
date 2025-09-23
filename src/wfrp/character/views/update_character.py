import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="character-update")
class UpdateCharacterViews(BaseView):
    def wounds_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Update Wounds")
        wounds_schema = colander.SchemaNode(
            colander.Mapping(),
            name="wounds",
        )
        wounds_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="wounds",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.wounds_current,
                missing="",
            )
        )
        schema.add(wounds_schema)
        return schema

    def wealth_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Update Money")
        wealth_schema = colander.SchemaNode(
            colander.Mapping(),
            name="wealth",
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="gold_crowns",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.gold_crowns,
                missing=0,
            )
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="silver_shillings",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.silver_shillings,
                missing=0,
            )
        )
        wealth_schema.add(
            colander.SchemaNode(
                colander.Integer(),
                name="brass_pennies",
                widget=deform.widget.TextInputWidget(style="width:100px;"),
                default=self.character.brass_pennies,
                missing=0,
            )
        )
        schema.add(wealth_schema)
        return schema

    def ambitions_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Update Ambitions")
        ambitions_schema = colander.SchemaNode(
            colander.Mapping(),
            name="ambition",
            description=(
                "Ambitions are a Character’s goals in life – what they want to "
                "achieve. All characters have both a Short-Term and Long-Term "
                "Ambition. You can change ambitions between sessions."
            ),
        )
        ambitions_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="short_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.short_term_ambition or "",
                missing="",
            )
        )
        ambitions_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="long_term_ambition",
                widget=deform.widget.TextAreaWidget(),
                validator=colander.Length(max=100),
                default=self.character.long_term_ambition or "",
                missing="",
            )
        )
        schema.add(ambitions_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):
        html = []
        all_forms = ["wounds", "wealth", "ambitions"]
        forms = {}
        for form in all_forms:
            button = f"Update {form.capitalize()}"
            attribute_schema = getattr(self, f"{form}_schema")()
            forms[f"{form}_form"] = deform.Form(
                attribute_schema,
                buttons=(button,),
                formid=f"{form}_form",
            )
        if "__formid__" in self.request.POST:
            form = forms[self.request.POST["__formid__"]]
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                for form in forms:
                    if form == self.request.POST["__formid__"]:
                        form_title = form.title().replace("_", " ")
                        message = f"{form_title} has an error"
                        self.request.session.flash(message, "error")
                        html.append(error.render())
                    else:
                        html.append(forms[form].render())
            else:
                message = self.update_character(form.formid, captured)
                self.request.session.flash(message, "success")
                url = self.request.route_url("character-update", id=self.character.id)
                return HTTPFound(location=url)
        else:
            for form in forms:
                html.append(forms[form].render())
        static_assets = list(forms.values())[0].get_widget_resources()
        return {
            "form": "".join(html),
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
            "character": self.character,
        }

    def update_character(self, form_id, captured):
        if form_id == "wounds_form":
            self.character.wounds_current = captured["wounds"]["wounds"]
            message = "You have updated your wounds"
        elif form_id == "wealth_form":
            self.character.brass_pennies = captured["wealth"]["brass_pennies"]
            self.character.silver_shillings = captured["wealth"]["silver_shillings"]
            self.character.gold_crowns = captured["wealth"]["gold_crowns"]
            message = "You have updated your wealth"
        elif form_id == "ambitions_form":
            self.character.short_term_ambition = captured["ambition"][
                "short_term_ambition"
            ]
            self.character.long_term_ambition = captured["ambition"][
                "long_term_ambition"
            ]
            message = "You have updated your ambitions"
        return message
