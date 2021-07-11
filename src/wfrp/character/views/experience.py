import itertools

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="experience")
class ExperienceViews(BaseView):
    def characteristic_schema(self):
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_advances = career_details["attributes"]
        schema = colander.SchemaNode(colander.Mapping(), title="Characteristics")
        characteristic_schema = colander.SchemaNode(
            colander.Mapping(),
            name="increase_characteristics",
            description=f"You have {self.character.experience} experience to spend",
        )
        choices = []
        for characteristic in career_advances:
            characteristic_lower = characteristic.lower().replace(" ", "_")
            current = getattr(self.character, characteristic_lower)
            advances = getattr(self.character, f"{characteristic_lower}_advances")
            choices.append(
                (
                    characteristic_lower,
                    f"{characteristic}({current}) - {advances} advances, "
                    f"{self.character.cost_characteristic(advances + 1)} "
                    "experience to increase",
                )
            )
        characteristic_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="characteristics",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description="Choose a characteristic to increase",
            )
        )
        schema.add(characteristic_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/name.pt")
    def form_view(self):
        html = []
        all_forms = ["characteristic"]
        forms = {}
        counter = itertools.count()
        for form in all_forms:
            attribute_schema = getattr(self, f"{form}_schema")()
            forms[f"{form}_form"] = deform.Form(
                attribute_schema,
                buttons=("Select Name",),
                formid=f"{form}_form",
                counter=counter,
            )
        if "Select_Name" in self.request.POST:
            form = forms[self.request.POST["__formid__"]]
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                attribute = captured["increase_characteristics"]["characteristics"]
                setattr(
                    self.character,
                    f"{attribute}_advances",
                    getattr(self.character, f"{attribute}_advances") + 1,
                )
                # attribute has increased, so this is the cost for getting to that value
                cost = self.character.cost_characteristic(
                    getattr(self.character, f"{attribute}_advances")
                )
                self.character.experience -= cost
                self.character.experience_spent += cost
                url = self.request.route_url("experience", uuid=self.character.uuid)
                self.character.status = {"complete": ""}
                return HTTPFound(location=url)
        else:
            for form in forms:
                html.append(forms[form].render())

        # just get the assets for the first form
        static_assets = list(forms.values())[0].get_widget_resources()
        return {
            "form": "".join(html),
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
