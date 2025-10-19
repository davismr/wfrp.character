import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CAREERS
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CLASS_DATA
from wfrp.character.data.careers.up_in_arms import get_sub_career
from wfrp.character.utils import roll_d100
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class SubCareerViews(BaseCreateView):
    def initialise_form(self):
        if self.character.create_data["sub-career"]:
            sub_career = self.character.create_data["sub-career"]
        else:
            sub_career = get_sub_career(self.character.career, roll_d100())
            self.character.create_data = {"sub-career": sub_career}
        if self.character.experience in [45, 70]:
            experience_loss = self.character.experience - 20
        elif self.character.experience in [25, 50]:
            experience_loss = self.character.experience
        else:
            experience_loss = 0
        return {"sub_career": sub_career, "experience_loss": experience_loss}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Specialist Career",
            description="Choose a specialist career from the list below.",
        )
        if data["experience_loss"]:
            description = (
                f"Your random roll is {data['sub_career']}, if you want to choose a "
                f"different specialist career you will lose {data['experience_loss']}"
                "XP from accepting the random career previously."
            )
        else:
            description = (
                "As you selected a career previously, you may choose a different "
                "specialist career."
            )
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Specialist Career",
            description=description,
            name="specialist_career",
        )
        career_choices = UP_IN_ARMS_CAREERS[self.character.career].values()
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                validator=colander.OneOf(career_choices),
                widget=deform.widget.RadioChoiceWidget(
                    values=[(x, x) for x in career_choices]
                ),
                default=data["sub_career"],
                name="specialist_career",
            )
        )
        schema.add(career_schema)
        return schema

    @view_config(route_name="sub-career")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema,
            buttons=["Choose Career"],
        )
        if "Choose_Career" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                career = captured["specialist_career"]["specialist_career"]
                career_data = UP_IN_ARMS_CLASS_DATA[career]
                career_title = list(career_data.keys())[0]
                self.character.career = career
                self.character.career_path = [career_title]
                self.character.career_title = career_title
                self.character.career_tier = career_data[career_title]["status"]["tier"]
                self.character.career_standing = career_data[career_title]["status"][
                    "standing"
                ]
                if data["experience_loss"] and career != data["sub_career"]:
                    self.character.experience += -data["experience_loss"]
                self.character.create_data = {"attributes": ""}
                url = self.request.route_url("attributes", id=self.character.id)
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
