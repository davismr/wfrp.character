import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.career_data import get_career
from wfrp.character.career_data import list_careers
from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="career")
class CareerViews(BaseView):
    def initialise_form(self):
        if self.character.status["career"]:
            career = self.character.status["career"]
        else:
            career = get_career(self.character.species, roll_d100())
            self.character.status = {"career": career}
        career_list = list_careers(self.character.species)
        career_choice = []
        for item in career.split(","):
            career_list.remove(item)
            career_choice.append(item)
        return {"career_choice": career_choice, "career_list": career_list}

    def reroll_career_view(self):
        career_choice = self.character.status["career"].split(",")
        while len(career_choice) < 3:
            career = get_career(self.character.species, roll_d100())
            if career not in career_choice:
                career_choice.append(career)
        self.character.status = {"career": ",".join(career_choice)}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Skills and Talents",
            validator=self.validate,
        )
        career_choices = []
        for item in data["career_choice"]:
            career_choices.append((item, item))
        if len(career_choices) == 1:
            description = (
                f"Accept {career_choices[0][0]} for 50XP, or reroll for 3 choices and "
                "25XP."
            )
        elif len(career_choices) == 3:
            description = (
                f"Accept {career_choices[0][0]}, {career_choices[1][0]} or "
                f"{career_choices[2][0]} for 25XP."
            )
        else:
            raise NotImplementedError("Incorrect number of career choices")
        career_choices.append(("", "Select a career below"))
        random_career_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career",
            description=description,
            name="random_career",
        )
        random_career_schema.add(
            colander.SchemaNode(
                colander.String(),
                validator=colander.OneOf([x[0] for x in career_choices]),
                widget=deform.widget.RadioChoiceWidget(values=career_choices),
                missing="",
                name="random_career",
            )
        )
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            name="career",
        )
        career_choices = [("", "Select a random career above")]
        for item in data["career_list"]:
            career_choices.append((item, item))
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                description="Choose a different career for no extra XP.",
                validator=colander.OneOf([x[0] for x in career_choices]),
                widget=deform.widget.RadioChoiceWidget(values=career_choices),
                missing="",
                name="career",
            )
        )
        schema.add(random_career_schema)
        schema.add(career_schema)
        return schema

    def validate(self, form, values):
        selected = []
        for item in values.keys():
            for value in values[item].keys():
                if values[item][value]:
                    selected.append(values[item][value])
        if len(selected) > 1:
            raise colander.Invalid(form, "You can only select a single career")
        elif not selected:
            raise colander.Invalid(form, "You have to select a career")
        if selected[0] not in list_careers(self.character.species):
            raise colander.Invalid(
                form, f"{selected[0]} is not available for {self.character.species}"
            )

    @view_config(renderer="wfrp.character:templates/career.pt")
    def form_view(self):
        if "Reroll" in self.request.POST:
            self.reroll_career_view()
        data = self.initialise_form()
        schema = self.schema(data)
        form_buttons = [
            "Choose Career",
        ]
        if len(data["career_choice"]) == 1:
            form_buttons.append("Reroll")
        form = deform.Form(
            schema,
            buttons=form_buttons,
        )

        if "Choose_Career" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                career = captured.get("random_career").get(
                    "random_career"
                ) or captured.get("career").get("career")
                career_choice = self.character.status["career"].split(",")
                if career in career_choice:
                    if len(career_choice) == 1:
                        self.character.experience += 50
                    else:
                        self.character.experience += 25
                self.character.career = career
                self.character.career_class = CAREER_DATA[career]["class"]
                career_level = list(CAREER_DATA[career].keys())[1]
                self.character.career_path.append(career_level)
                self.character.career_title = career_level
                self.character.career_tier = CAREER_DATA[career][career_level][
                    "status"
                ]["tier"]
                self.character.career_standing = CAREER_DATA[career][career_level][
                    "status"
                ]["standing"]
                url = self.request.route_url("attributes", uuid=self.character.uuid)
                self.character.status = {"attributes": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
