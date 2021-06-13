import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.views.attributes import ATTRIBUTES
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="advances")
class AdvancesViews(BaseView):
    def initialise_form(self):
        attributes = {}
        for attribute in ATTRIBUTES:
            attribute_lower = f'{attribute.lower().replace(" ", "_")}_initial'
            attributes[attribute] = getattr(self.character, attribute_lower)
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_advances = career_details["attributes"]
        return {"attributes": attributes, "advances": career_advances}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Advance characteristics",
        )
        advances_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Attributes",
            validator=self.validate,
            description=(
                "You can allocate a total of 5 Advances across these Characteristics"
            ),
        )
        # TODO add some field validation, each must be <=5 and should be int field
        for advance in data["advances"]:
            advances_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    missing="",
                    widget=deform.widget.TextInputWidget(),
                    name=advance,
                )
            )
        schema.add(advances_schema)
        return schema

    def validate(self, form, values):
        total = 0
        for value in values:
            if values[value]:
                total += int(values[value])
        if total > 5:
            raise colander.Invalid(form, "You can only add a total of 5 advances")
        elif total < 5:
            raise colander.Invalid(form, "You have to add a total of 5 advances")

    @view_config(renderer=__name__ + ":../templates/advances.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema,
            buttons=("Accept Advances",),
        )

        if "Accept_Advances" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                for advance in captured[""]:
                    if not captured[""][advance]:
                        continue
                    attribute_lower = f'{advance.lower().replace(" ", "_")}_advances'
                    current_value = getattr(self.character, attribute_lower)
                    new_value = current_value + int(captured[""][advance])
                    setattr(self.character, attribute_lower, new_value)
                url = self.request.route_url("species_skills", uuid=self.character.uuid)
                self.character.status = {"species_skills": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
