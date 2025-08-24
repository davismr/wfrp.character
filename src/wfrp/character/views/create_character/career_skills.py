import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.careers.careers import CAREER_DATA
from wfrp.character.data.careers.careers import CAREER_DATA_WITH_SEAFARER
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/skills.pt", permission="create_character"
)
class CareerSkillsViews(BaseCreateView):
    def initialise_form(self):
        if "sea_of_claws" in self.character.expansions:
            career_data = CAREER_DATA_WITH_SEAFARER[self.character.career]
        else:
            career_data = CAREER_DATA[self.character.career]
        career_details = career_data[self.character.career_title]
        career_skills = career_details["skills"]
        career_talents = career_details["talents"]
        return {"career_skills": career_skills, "career_talents": career_talents}

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(), title="Career Skills and Talents"
        )
        skill_schema = colander.SchemaNode(
            colander.Mapping(),
            description=(
                "Allocate 40 Advances to your eight starting Skills, with no more than "
                "10 Advances allocated to any single Skill at this stage."
            ),
            validator=self.validate,
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
                    description="(Any)" in skill
                    and "Choose the specialisation below"
                    or "",
                    name=skill,
                )
            )
            if "(Any)" in skill or " or " in skill:
                specialisation_choices = []
                if "(Any)" in skill:
                    choices = SKILL_DATA[skill.split(" (")[0]]["specialisations"]
                else:
                    choices = skill.split("(")[1].replace(")", "").split(" or ")
                for item in choices:
                    specialisation_choices.append((item, item))
                skill_schema.add(
                    colander.SchemaNode(
                        colander.String(),
                        validator=colander.OneOf(
                            [x[0] for x in specialisation_choices]
                        ),
                        widget=deform.widget.RadioChoiceWidget(
                            values=specialisation_choices, inline=True
                        ),
                        missing="",
                        name=f"{skill} specialisation",
                    )
                )

        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            description=("You may choose a single Talent to learn."),
            name="career_talents",
        )
        talent_choices = []
        for item in data["career_talents"]:
            if "(Any)" in item:
                item = item.replace(" (Any)", "")
                for specialisation in TALENT_DATA[item]["specialisations"]:
                    talent_choices.append(
                        (f"{item} ({specialisation})", f"{item} ({specialisation})")
                    )
            else:
                talent_choices.append((item, item))
        talent_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="career_talent",
                validator=colander.OneOf([x[0] for x in talent_choices]),
                widget=deform.widget.RadioChoiceWidget(values=talent_choices),
                default=talent_choices[0][0],
            )
        )
        schema.add(skill_schema)
        schema.add(talent_schema)
        return schema

    def validate(self, form, values):
        total = 0
        for value in values:
            if not values[value]:
                # ignore zeros and empty strings
                continue
            try:
                total += values[value]
            except TypeError:
                # ignore talent and specialisation strings
                continue
            if ("(Any)" in value or " or " in value) and not values[
                f"{value} specialisation"
            ]:
                raise colander.Invalid(
                    form, f"You have to select a specialisation for {value}"
                )
        if total > 40:
            raise colander.Invalid(
                form, f"You can only allocate 40 advances, you have allocated {total}"
            )
        elif total < 40:
            raise colander.Invalid(
                form,
                f"You must allocate all 40 advances, you have only allocated {total}",
            )

    @view_config(route_name="career-skills")
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
                self.update_values(captured)
                url = self.request.route_url("trappings", id=self.character.id)
                self.character.status = {"trappings": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        form_data = {"skills": {}, "talents": {}}
        for skill in data["career_skills"]:
            if skill in SKILL_DATA:
                form_data["skills"][skill] = SKILL_DATA[skill]
            else:
                form_data["skills"][skill] = SKILL_DATA[skill.split(" (")[0]]
        for talent in data["career_talents"]:
            if talent in TALENT_DATA:
                form_data["talents"][talent] = TALENT_DATA[talent]
            else:
                form_data["talents"][talent] = TALENT_DATA[talent.split(" (")[0]]
        return {
            "form": html,
            "form_data": form_data,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    def update_values(self, captured):
        for item in captured["career_skills"]:
            value = captured["career_skills"].get(item)
            if not value or "specialisation" in item:
                continue
            if "(Any)" in item:
                specialisation = captured["career_skills"].get(f"{item} specialisation")
                self.character.skills[item.replace("Any", specialisation)] = int(value)
            elif " or " in item:
                specialisation = captured["career_skills"].get(f"{item} specialisation")
                option = item.split("(")[1].replace(")", "")
                self.character.skills[item.replace(option, specialisation)] = int(value)
            else:
                self.character.skills[item] = int(value)
        for item in captured["career_talents"]:
            value = captured["career_talents"].get(item)
            self.character.talents[value] = 1
