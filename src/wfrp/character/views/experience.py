import itertools

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="experience")
class ExperienceViews(BaseView):
    def initialise_form(self):
        self.career_level = self.character.career_level()
        self.career_data = self.character.career_data()
        self.career_details = self.career_data[self.character.career_title]
        self.completed_career = self.character.completed_career()

    def characteristic_schema(self):
        characteristics = []
        for index, career_level in enumerate(self.career_data.values()):
            for characteristic in career_level["attributes"]:
                characteristics.append(characteristic)
            if index == self.career_level - 1:
                break
        schema = colander.SchemaNode(colander.Mapping(), title="Characteristics")
        characteristic_schema = colander.SchemaNode(
            colander.Mapping(),
            name="increase_characteristic",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_characteristic,
        )
        choices = [("", "None")]
        for characteristic in characteristics:
            characteristic_lower = characteristic.lower().replace(" ", "_")
            current = getattr(self.character, characteristic_lower)
            advances = getattr(self.character, f"{characteristic_lower}_advances")
            choices.append(
                (
                    characteristic_lower,
                    f"{characteristic} ({current}) - {advances} advances, "
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
                f"You do not have enough experience to increase "
                f"{characteristic_display}, you need {cost} XP",
            )

    def skill_schema(self):  # noqa: C901
        career_skills = []
        for index, career_level in enumerate(self.career_data.values()):
            if index == self.career_level:
                break
            for skill in career_level["skills"]:
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
        choices = [("", "None")]
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
                f"You do not have enough experience to increase {skill}, "
                f"you need {cost} XP",
            )

    def talent_schema(self):
        career_talents = self.career_details["talents"]
        schema = colander.SchemaNode(colander.Mapping(), title="Talents")
        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            name="add_talent",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_talent,
        )
        choices = [("", "None")]
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
                f"You do not have enough experience to increase {talent}, "
                f"you need {cost} XP",
            )

    def career_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Career")
        if self.completed_career is True:
            cost = 100
            description = (
                "You have completed your current career level and have "
                f"{self.character.experience} experience to spend"
            )
        else:
            cost = 200
            description = (
                "You have not completed your current career level and have "
                f"{self.character.experience} experience to spend"
            )
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            name="change_career",
            description=description,
            validator=self.validate_career,
        )
        choices = [("", "None")]
        for index, career in enumerate(self.career_data.keys()):
            if career == self.character.career_title:
                continue
            choices.append((f"{career}", f"{career} (level {index + 1}), {cost} XP"))
            if index == self.career_level:
                break
        career_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="advance_career",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description="Choose a Career level",
            )
        )
        schema.add(career_schema)
        return schema

    def validate_career(self, form, values):
        cost = 200
        if self.completed_career is True:
            cost = 100
        if cost > self.character.experience:
            raise colander.Invalid(
                form,
                "You do not have enough experience to change career, "
                f"you need {cost} XP",
            )

    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):
        self.initialise_form()
        html = []
        all_forms = ["characteristic", "skill", "talent", "career"]
        forms = {}
        counter = itertools.count()
        for form in all_forms:
            if form != "career":
                button = f"Increase {form}"
            else:
                button = "Change Career"
            attribute_schema = getattr(self, f"{form}_schema")()
            forms[f"{form}_form"] = deform.Form(
                attribute_schema,
                buttons=(button,),
                formid=f"{form}_form",
                counter=counter,
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

    def update_character(self, form_id, captured):
        if form_id == "characteristic_form":
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
            message = f"You have spent {cost}XP to increase {attribute} by 1"
        elif form_id == "skill_form":
            skill = captured["increase_skill"]["skill"]
            if skill in self.character.skills:
                self.character.skills[skill] += 1
            else:
                self.character.skills[skill] = 1
            cost = self.character.cost_skill(self.character.skills[skill])
            message = f"You have spent {cost}XP to increase {skill} by 1"
        elif form_id == "talent_form":
            talent = captured["add_talent"]["talent"]
            if talent in self.character.talents:
                self.character.talents[talent] += 1
            else:
                self.character.talents[talent] = 1
            cost = self.character.cost_talent(self.character.talents[talent])
            message = f"You have spent {cost}XP to increase {talent} by 1"
        elif form_id == "career_form":
            new_career = captured["change_career"]["advance_career"]
            self.character.career_title = new_career
            self.character.career_path.append(new_career)
            cost = 200
            if self.completed_career:
                cost = 100
            message = f"You have spent {cost}XP to advance career to {new_career}"
        self.character.experience -= cost
        self.character.experience_spent += cost
        return message
