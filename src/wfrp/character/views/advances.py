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
            name="attributes",
            validator=self.validate,
            description=(
                "You can allocate a total of 5 Advances across these Characteristics"
            ),
        )
        advances_choices = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ]
        for advance in data["advances"]:
            advances_schema.add(
                colander.SchemaNode(
                    colander.Int(),
                    name=advance,
                    description=(
                        f"{advance} is currently "
                        f"{getattr(self.character, advance.lower().replace(' ', '_'))}"
                    ),
                    validator=colander.OneOf([x[0] for x in advances_choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=advances_choices, inline=True
                    ),
                    default=0,
                )
            )
        schema.add(advances_schema)
        fate_schema = colander.SchemaNode(
            colander.Mapping(),
            name="fate & resilience",
            validator=self.validate_fate,
            description=(
                f"You can spread {self.character.extra_points} points across "
                "fate and fortune"
            ),
        )
        fate_choices = [(i, i) for i in range(self.character.extra_points + 1)]
        fate_schema.add(
            colander.SchemaNode(
                colander.Int(),
                name="fate",
                description=(f"Fate is currently {self.character.fate}"),
                validator=colander.OneOf([x[0] for x in fate_choices]),
                widget=deform.widget.RadioChoiceWidget(
                    values=fate_choices, inline=True
                ),
                default=0,
            )
        )
        fate_schema.add(
            colander.SchemaNode(
                colander.Int(),
                name="resilience",
                description=(f"Resilience is currently {self.character.resilience}"),
                validator=colander.OneOf([x[0] for x in fate_choices]),
                widget=deform.widget.RadioChoiceWidget(
                    values=fate_choices, inline=True
                ),
                default=0,
            )
        )
        schema.add(fate_schema)
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

    def validate_fate(self, form, values):
        total = 0
        for value in values:
            if values[value]:
                total += int(values[value])
        total_allowed = self.character.extra_points
        if total > total_allowed:
            raise colander.Invalid(
                form,
                f"You can only spread {total_allowed} points between "
                "fate and resilience",
            )
        elif total < self.character.extra_points:
            raise colander.Invalid(
                form,
                f"You have to spread {total_allowed} points between "
                "fate and resilience",
            )

    @view_config(renderer="wfrp.character:templates/advances.pt")
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
                for advance in captured["attributes"]:
                    attribute_lower = f'{advance.lower().replace(" ", "_")}_advances'
                    current_value = getattr(self.character, attribute_lower)
                    new_value = current_value + captured["attributes"][advance]
                    setattr(self.character, attribute_lower, new_value)
                self.character.fate = (
                    self.character.fate + captured["fate & resilience"]["fate"]
                )
                self.character.resilience = (
                    self.character.resilience
                    + captured["fate & resilience"]["resilience"]
                )
                self.character.fortune = self.character.fate
                self.character.resolve = self.character.resilience
                self.character.extra_points = 0
                url = self.request.route_url("species_skills", uuid=self.character.uuid)
                self.character.status = {"species_skills": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        return {
            "character": self.character,
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
