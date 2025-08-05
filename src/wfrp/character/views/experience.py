import itertools

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.careers.careers import CAREER_DATA
from wfrp.character.data.skills import SKILL_DATA
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
            name="increase_characteristic",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_characteristic,
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
                name="characteristic",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description="Choose a characteristic to increase",
            )
        )
        schema.add(characteristic_schema)
        return schema

    def validate_characteristic(self, form, values):
        characteristic = values["characteristic"]
        cost = self.character.cost_characteristic(
            getattr(self.character, f"{characteristic}_advances") + 1
        )
        if cost > self.character.experience:
            characteristic_display = characteristic.replace("_", " ").title()
            raise colander.Invalid(
                form,
                f"You do not have enought experience to increase "
                f"{characteristic_display}, you need {cost} XP",
            )

    def skill_schema(self):  # noqa: C901
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_skills = []
        for skill in career_details["skills"]:
            if " or " in skill:
                # TODO this needs to be refactored
                root_skill = skill.split(" (")[0]
                specialisations = skill.split(" (")[1][:-1].split(" or ")
                for specialisation in specialisations:
                    if f"{root_skill} ({specialisation})" in self.character.skills:
                        career_skills.append(f"{root_skill} ({specialisation})")
                        break
                else:
                    for specialisation in specialisations:
                        career_skills.append(f"{root_skill} ({specialisation})")
            elif "(Any)" in skill:
                current_skills_length = len(career_skills)
                # TODO this should not allow increases in species skills
                # eg Human Pit Fighter can take Melee(Basic) as species skill
                # and has Melee(Any) but second stage career explicitly includes
                # Melee (Basic)
                root_skill = skill.split(" (")[0]
                for existing_skill in self.character.skills:
                    if existing_skill.startswith(root_skill):
                        career_skills.append(existing_skill)
                if len(career_skills) == current_skills_length:
                    # none chosen yet, so add all to allow a choice
                    for specialisation in SKILL_DATA[root_skill]["specialisations"]:
                        career_skills.append(f"{root_skill} ({specialisation})")
            else:
                career_skills.append(skill)
        # deduplicate the list, then sort it again
        career_skills = sorted(list(set(career_skills)))
        schema = colander.SchemaNode(colander.Mapping(), title="Skills")
        skill_schema = colander.SchemaNode(
            colander.Mapping(),
            name="increase_skill",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_skill,
        )
        choices = []
        for skill in career_skills:
            try:
                advances = self.character.skills[skill]
            except KeyError:
                advances = 0
            choices.append(
                (
                    skill,
                    f"{skill} ({advances}), "
                    f"{self.character.cost_skill(advances + 1)} experience to increase",
                )
            )
        skill_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="skill",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description="Choose a skill to increase",
            )
        )
        schema.add(skill_schema)
        return schema

    def validate_skill(self, form, values):
        skill = values["skill"]
        if skill in self.character.skills:
            cost = self.character.cost_skill(self.character.skills[skill] + 1)
        else:
            cost = self.character.cost_skill(1)
        if cost > self.character.experience:
            raise colander.Invalid(
                form,
                f"You do not have enought experience to increase {skill}, "
                f"you need {cost} XP",
            )

    def talent_schema(self):
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_talents = career_details["talents"]
        schema = colander.SchemaNode(colander.Mapping(), title="talents")
        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            name="add_talent",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_talent,
        )
        choices = []
        for talent in career_talents:
            try:
                advances = self.character.talents[talent]
            except KeyError:
                advances = 0
            choices.append(
                (
                    talent,
                    f"{talent} ({advances}), {self.character.cost_talent(advances + 1)}"
                    f" experience to increase",
                )
            )
        talent_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="talent",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description="Choose a talent to increase",
            )
        )
        schema.add(talent_schema)
        return schema

    def validate_talent(self, form, values):
        talent = values["talent"]
        if talent in self.character.talents:
            cost = self.character.cost_talent(self.character.talents[talent] + 1)
        else:
            cost = self.character.cost_talent(1)
        if cost > self.character.experience:
            raise colander.Invalid(
                form,
                f"You do not have enought experience to increase {talent}, "
                f"you need {cost} XP",
            )

    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):  # noqa: C901
        html = []
        all_forms = ["characteristic", "skill", "talent"]
        forms = {}
        counter = itertools.count()
        for form in all_forms:
            attribute_schema = getattr(self, f"{form}_schema")()
            forms[f"{form}_form"] = deform.Form(
                attribute_schema,
                buttons=(f"Increase {form}",),
                formid=f"{form}_form",
                counter=counter,
            )
        if "__formid__" in self.request.POST:
            form = forms[self.request.POST["__formid__"]]
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if form.formid == "characteristic_form":
                    attribute = captured["increase_characteristic"]["characteristic"]
                    setattr(
                        self.character,
                        f"{attribute}_advances",
                        getattr(self.character, f"{attribute}_advances") + 1,
                    )
                    # attribute has increased, so this is the cost for getting there
                    cost = self.character.cost_characteristic(
                        getattr(self.character, f"{attribute}_advances")
                    )
                elif form.formid == "skill_form":
                    skill = captured["increase_skill"]["skill"]
                    if skill in self.character.skills:
                        self.character.skills[skill] += 1
                    else:
                        self.character.skills[skill] = 1
                    cost = self.character.cost_skill(self.character.skills[skill])
                elif form.formid == "talent_form":
                    talent = captured["add_talent"]["talent"]
                    if talent in self.character.talents:
                        self.character.talents[talent] += 1
                    else:
                        self.character.talents[talent] = 1
                    cost = self.character.cost_talent(self.character.talents[talent])
                self.character.experience -= cost
                self.character.experience_spent += cost
                url = self.request.route_url("experience", id=self.character.id)
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
            "character": self.character,
        }
