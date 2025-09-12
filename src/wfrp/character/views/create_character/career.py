import colander
import deform
from deform.widget import OptGroup
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.careers.careers import CAREER_BY_CLASS
from wfrp.character.data.careers.careers import CAREER_BY_CLASS_WITH_SEAFARER
from wfrp.character.data.careers.careers import CAREER_DATA
from wfrp.character.data.careers.careers import CAREER_DATA_WITH_SEAFARER
from wfrp.character.data.careers.tables import get_career
from wfrp.character.data.careers.tables import list_careers
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CAREERS
from wfrp.character.utils import roll_d100
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class CareerViews(BaseCreateView):
    def __init__(self, request):
        super().__init__(request)
        self.sea_of_claws = False
        if "sea_of_claws" in self.character.expansions:
            self.sea_of_claws = True

    def initialise_form(self):
        if self.character.status["career"]:
            careers = self.character.status["career"]
        else:
            career = get_career(self.character.species, roll_d100(), self.sea_of_claws)
            careers = [career]
            self.character.status = {"career": careers}
        if self.sea_of_claws:
            career_list = list_careers(self.character.species, True)
        else:
            career_list = list_careers(self.character.species)
        career_choice = []
        for item in careers:
            career_list.remove(item)
            career_choice.append(item)
        return {"career_choice": career_choice, "career_list": career_list}

    def reroll_career_view(self):
        career_choice = self.character.status["career"]
        while len(career_choice) < 3:
            career = get_career(self.character.species, roll_d100(), self.sea_of_claws)
            if career not in career_choice:
                career_choice.append(career)
        # need to add a key so sqlalchemy will detect a change
        self.character.status = {"career": career_choice, "reroll": True}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Skills and Talents",
            validator=self.validate,
        )
        career_choices = []
        for item in data["career_choice"]:
            if self.sea_of_claws:
                career_choices.append(
                    (item, f"{item} ({CAREER_BY_CLASS_WITH_SEAFARER[item]})")
                )
            else:
                career_choices.append((item, f"{item} ({CAREER_BY_CLASS[item]})"))
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
        career_list = {}
        for career in data["career_list"]:
            if self.sea_of_claws:
                career_list.setdefault(
                    CAREER_BY_CLASS_WITH_SEAFARER[career], []
                ).append((career, career))
            else:
                career_list.setdefault(CAREER_BY_CLASS[career], []).append(
                    (career, career)
                )
        for career_class in career_list:
            career_choices.append(OptGroup(career_class, *career_list[career_class]))
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                description="Choose a different career for no extra XP.",
                validator=colander.OneOf(data["career_list"]),
                widget=deform.widget.SelectWidget(values=career_choices),
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
        if not selected:
            raise colander.Invalid(form, "You have to select a career")

    @view_config(route_name="career")
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
                career_choice = self.character.status["career"]
                if career in career_choice:
                    if len(career_choice) == 1:
                        self.character.experience += 50
                    else:
                        self.character.experience += 25
                self.character.career = career
                if self.sea_of_claws:
                    self.character.career_class = CAREER_BY_CLASS_WITH_SEAFARER[career]
                    career_data = CAREER_DATA_WITH_SEAFARER[career]
                else:
                    self.character.career_class = CAREER_BY_CLASS[career]
                    career_data = CAREER_DATA[career]
                career_title = list(career_data.keys())[0]
                self.character.career_path.append(career_title)
                self.character.career_title = career_title
                self.character.career_tier = career_data[career_title]["status"]["tier"]
                self.character.career_standing = career_data[career_title]["status"][
                    "standing"
                ]
                url = self.get_next_url()
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

    def get_next_url(self):
        if (
            "up_in_arms" in self.character.expansions
            and self.character.career in UP_IN_ARMS_CAREERS
        ):
            self.character.status = {"sub-career": ""}
            return self.request.route_url("sub-career", id=self.character.id)
        self.character.status = {"attributes": ""}
        return self.request.route_url("attributes", id=self.character.id)
