import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="career_skills")
class CareerSkillsViews(BaseView):
    def initialise_form(self):
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_skills = career_details["skills"]
        career_talents = career_details["talents"]
        return {"career_skills": career_skills, "career_talents": career_talents}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(), title="Career Skills and Talents"
        )
        skill_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Skills",
            description=(
                "Allocate 40 Advances to your eight starting Skills, with no more than "
                "10 Advances allocated to any single Skill at this stage."
            ),
            validator=None,
            name="career_skills",
        )
        skill_choices = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
        ]
        for skill in data["career_skills"]:
            skill_schema.add(
                colander.SchemaNode(
                    colander.Int(),
                    validator=colander.OneOf([x[0] for x in skill_choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=skill_choices, inline=True
                    ),
                    default=0,
                    name=skill,
                )
            )

        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Talents",
            description=("You may choose a single Talent to learn."),
            name="career_talents",
        )
        talent_choices = []
        for item in data["career_talents"]:
            talent_choices.append((item, item))
        talent_schema.add(
            colander.SchemaNode(
                colander.String(),
                validator=colander.OneOf([x[0] for x in talent_choices]),
                widget=deform.widget.RadioChoiceWidget(values=talent_choices),
                default=talent_choices[0][0],
                name="career_talent",
            )
        )
        schema.add(skill_schema)
        schema.add(talent_schema)
        return schema

    @view_config(renderer=__name__ + ":../templates/career_skills.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(schema, buttons=("Choose Skills",))

        if "Choose_Skills" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                for item in captured["career_skills"]:
                    value = captured["career_skills"].get(item)
                    if value == 0:
                        continue
                    self.character.skills[item] = int(value)
                for item in captured["career_talents"]:
                    value = captured["career_talents"].get(item)
                    self.character.talents.append(value)
                url = self.request.route_url("trappings", uuid=self.character.uuid)
                self.character.status = {"trappings": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
