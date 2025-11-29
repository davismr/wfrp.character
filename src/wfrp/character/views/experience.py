import itertools

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.magic.arcane import ARCANE_MAGIC_DATA
from wfrp.character.data.magic.chanty import CHANTY_DATA
from wfrp.character.data.magic.colour_magic import get_colour_spells
from wfrp.character.data.magic.miracles import get_miracles
from wfrp.character.data.magic.petty import PETTY_MAGIC_DATA
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.models.experience import ExperienceCost
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
                    f"{self.character.cost_characteristic(advances)} "
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

    def validate_characteristic(self, node, values):
        characteristic = values["characteristic"]
        cost = self.character.cost_characteristic(
            getattr(self.character, f"{characteristic}_advances")
        )
        if cost > self.character.experience:
            characteristic_display = characteristic.replace("_", " ").title()
            raise colander.Invalid(
                node,
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
                elif "(Any)" in skill or "(Any Colour)" in skill:
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
                    f"{self.character.cost_skill(advances)} experience to increase",
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

    def validate_skill(self, node, values):
        skill = values["skill"]
        if skill in self.character.skills:
            cost = self.character.cost_skill(self.character.skills[skill])
        else:
            cost = self.character.cost_skill(1)
        if cost > self.character.experience:
            raise colander.Invalid(
                node,
                f"You do not have enough experience to increase {skill}, "
                f"you need {cost} XP",
            )

    def talent_schema(self):  # noqa: C901
        career_talents = self.career_details["talents"]
        schema = colander.SchemaNode(colander.Mapping(), title="Talents")
        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            name="add_talent",
            description=f"You have {self.character.experience} experience to spend",
            validator=self.validate_talent,
        )
        choices = [("", "None")]
        choice_talents = []
        for talent in career_talents:
            if talent == "Chanty" and "Chanty" in self.character.talents:
                continue
            elif "(Any)" in talent or "(Any Arcane Lore)" in talent:
                talent_root = talent.split(" (")[0]
                for item in self.character.talents:
                    if item.startswith(talent_root):
                        talent = item
                        break
                else:
                    choice_talents.append(talent)
            try:
                advances = self.character.talents[talent]
            except KeyError:
                advances = 0
            if not self.check_talent_max(talent, advances):
                choices.append(
                    (
                        talent,
                        f"{talent} ({advances}), "
                        f"{self.character.cost_talent(advances)} experience to "
                        "increase",
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
        for item in choice_talents:
            specialisation_choices = []
            choices = TALENT_DATA[item.split(" (")[0]]["specialisations"]
            for choice in choices:
                specialisation_choices.append((choice, choice))
            talent_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    validator=colander.OneOf([x[0] for x in specialisation_choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=specialisation_choices, inline=True
                    ),
                    missing="",
                    name=f"{item} specialisation",
                )
            )
        schema.add(talent_schema)
        return schema

    def check_talent_max(self, talent, advances):
        talent_data = TALENT_DATA[talent.split(" (")[0]]
        if "max" not in talent_data:
            return False
        max = talent_data["max"]
        if max is None:
            return True
        elif isinstance(max, int):
            if advances >= max:
                return True
        elif "Bonus" in max:
            characteristic = max.replace(" Bonus", "").replace(" ", "_").lower()
            max_bonus = getattr(self.character, characteristic) // 10
            if advances >= max_bonus:
                return True
        return False

    def validate_talent(self, node, values):
        talent = values["talent"]
        if "(Any" in talent and not values[f"{talent} specialisation"]:
            error = colander.Invalid(node, "You have to select a specialisation")
            error[f"{talent} specialisation"] = (
                f"You have to select a specialisation for {talent}"
            )
            raise error
        if talent in self.character.talents:
            cost = self.character.cost_talent(self.character.talents[talent])
        else:
            cost = self.character.cost_talent(0)
        if cost > self.character.experience:
            raise colander.Invalid(
                node,
                f"You do not have enough experience to increase {talent}, "
                f"you need {cost} XP",
            )

    def chanties_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Chanties")
        chanties = self.character.chanties
        chanties_schema = colander.SchemaNode(
            colander.Mapping(),
            name="chanties",
            description=(
                f"You can have a maximum of {self.character.intelligence // 10} "
                f"chanties and  have learned {len(chanties)} chanties; "
                f"{', '.join(chanties)}. "
                f"You have {self.character.experience} experience to spend"
            ),
            validator=self.validate_chanties,
        )
        choices = [("", "None")]
        for chanty in CHANTY_DATA:
            if chanty not in chanties:
                choices.append((chanty, chanty))
        chanties_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="chanty",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description=(
                    "Choose a Chanty to Learn, this costs " f"{self.cost_chanty()} XP"
                ),
            )
        )
        schema.add(chanties_schema)
        return schema

    def cost_chanty(self):
        return 100 + (100 * len(self.character.chanties))

    def validate_chanties(self, node, values):
        if len(self.character.chanties) >= self.character.intelligence // 10:
            raise colander.Invalid(
                node,
                "You have learned the maximum of chanties, to learn more you need to "
                "increase your intelligence bonus",
            )
        cost = self.character.cost_miracle()
        if cost > self.character.experience:
            raise colander.Invalid(
                node,
                "You do not have enough experience to change career, "
                f"you need {cost} XP",
            )

    def magic_schema(self):  # noqa: C901
        schema = colander.SchemaNode(colander.Mapping(), title="Spells")
        petty_magic_spells = self.character.petty_magic
        spell_schema = colander.SchemaNode(
            colander.Mapping(),
            name="spells",
            description=(
                f"You have a willpower of {self.character.willpower} and have learned "
                f"{len(petty_magic_spells)} petty magic spells; "
                f"{', '.join(petty_magic_spells)}. "
                f"{len(self.character.arcane_magic)} arcane magic spells; "
                f"{', '.join(self.character.arcane_magic)}. "
                f"{len(self.character.lore_magic)} lore magic spells; "
                f"{', '.join(self.character.lore_magic)}. "
                f"You have {self.character.experience} experience to spend"
            ),
            validator=self.validate_magic,
        )
        if "Petty Magic" in self.character.talents:
            choices = [("", "None")]
            for spell in PETTY_MAGIC_DATA:
                if spell in petty_magic_spells:
                    continue
                choices.append((spell, spell))
            spell_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name="petty_magic",
                    widget=deform.widget.RadioChoiceWidget(values=choices),
                    validator=colander.OneOf([x[0] for x in choices]),
                    missing="",
                    description=(
                        "Choose a Petty Magic Spell to Learn, this costs "
                        f"{self.character.spell_cost('petty_magic')} XP"
                    ),
                )
            )
        arcane_available = False
        for talent in self.character.talents:
            if talent.startswith("Arcane Magic ("):
                arcane_available = True
                arcane_spells = get_colour_spells(talent.split("(")[1].replace(")", ""))
        if arcane_available:
            choices = [("", "None")]
            for spell in ARCANE_MAGIC_DATA:
                if spell in self.character.arcane_magic:
                    continue
                choices.append((spell, spell))
            spell_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name="arcane_magic",
                    widget=deform.widget.RadioChoiceWidget(values=choices),
                    validator=colander.OneOf([x[0] for x in choices]),
                    missing="",
                    description=(
                        "Choose an Arcane Magic Spell to Learn, this costs "
                        f"{self.character.spell_cost('arcane_magic')} XP"
                    ),
                )
            )
            choices = [("", "None")]
            for spell in arcane_spells:
                if spell in self.character.lore_magic:
                    continue
                choices.append((spell, spell))
            spell_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name="lore_magic",
                    widget=deform.widget.RadioChoiceWidget(values=choices),
                    validator=colander.OneOf([x[0] for x in choices]),
                    missing="",
                    description=(
                        "Choose a Lore Magic Spell to Learn, this costs "
                        f"{self.character.spell_cost('lore_magic')} XP"
                    ),
                )
            )
        schema.add(spell_schema)
        return schema

    def validate_magic(self, node, values):
        error = colander.Invalid(node, "Error message on form")
        items = {k: v for k, v in values.items() if v}
        if len(items) == 0:
            error.msg = "You have to select a spell to learn"
            for field in values:
                error[field] = "You have to select a spell to learn"
            raise error
        if len(items) != 1:
            error.msg = "You can only select one spell to learn"
            for field in items:
                error[field] = "You can only select one spell to learn"
            raise error
        spell_type = list(items.keys())[0]
        cost = self.character.spell_cost(spell_type)
        if cost > self.character.experience:
            error.msg = (
                "You do not have enough experience to learn this spell, "
                f"you need {cost} XP"
            )
            error[spell_type] = error.msg
            raise error

    def miracles_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Miracles")
        miracles = self.character.miracles
        miracles_schema = colander.SchemaNode(
            colander.Mapping(),
            name="miracles",
            description=(
                f"You have learned {len(miracles)} miracles; {', '.join(miracles)}. "
                f"You have {self.character.experience} experience to spend"
            ),
            validator=self.validate_miracles,
        )
        for talent in self.character.talents:
            if talent.startswith("Invoke ("):
                all_miracles = get_miracles(
                    talent.split("Invoke (")[1].replace(")", "")
                )
                break
        choices = [("", "None")]
        for miracle in all_miracles:
            if miracle not in miracles:
                choices.append((miracle, miracle))
        miracles_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="miracle",
                widget=deform.widget.RadioChoiceWidget(values=choices),
                validator=colander.OneOf([x[0] for x in choices]),
                description=(
                    "Choose a Miracle to Learn, this costs "
                    f"{self.character.cost_miracle()} XP"
                ),
            )
        )
        schema.add(miracles_schema)
        return schema

    def validate_miracles(self, node, values):
        cost = self.character.cost_miracle()
        if cost > self.character.experience:
            raise colander.Invalid(
                node,
                "You do not have enough experience to change career, "
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

    def validate_career(self, node, values):
        cost = 200
        if self.completed_career is True:
            cost = 100
        if cost > self.character.experience:
            raise colander.Invalid(
                node,
                "You do not have enough experience to change career, "
                f"you need {cost} XP",
            )

    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):  # noqa: C901
        self.initialise_form()
        html = []
        all_forms = [
            "characteristic",
            "skill",
            "talent",
            "chanties",
            "magic",
            "miracles",
            "career",
        ]
        for talent in self.character.talents:
            if talent.startswith("Invoke ("):
                break
        else:
            all_forms.remove("miracles")
        if "Chanty" not in self.character.talents:
            all_forms.remove("chanties")
        for talent in self.character.talents:
            if talent == "Petty Magic" or talent.startswith("Arcane Magic ("):
                break
        else:
            all_forms.remove("magic")
        forms = {}
        counter = itertools.count()
        for form in all_forms:
            if form == "career":
                button = "Change Career"
            elif form == "chanties":
                button = "Learn Chanty"
            elif form == "magic":
                button = "Learn Spell"
            elif form == "miracles":
                button = "Learn Miracle"
            else:
                button = f"Increase {form}"
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
                url = self.update_character(form.formid, captured)
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

    def update_character(self, form_id, captured):  # noqa: C901
        if form_id == "characteristic_form":
            attribute = captured["increase_characteristic"]["characteristic"]
            cost = self.character.cost_characteristic(
                getattr(self.character, f"{attribute}_advances")
            )
            setattr(
                self.character,
                f"{attribute}_advances",
                getattr(self.character, f"{attribute}_advances") + 1,
            )
            experience_cost = ExperienceCost(
                character_id=self.character.id,
                type="characteristic",
                cost=cost,
                name=attribute,
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to increase {attribute} by 1"
        elif form_id == "skill_form":
            skill = captured["increase_skill"]["skill"]
            cost = self.character.cost_skill(self.character.skills.get(skill, 0))
            if skill in self.character.skills:
                self.character.skills[skill] += 1
            else:
                self.character.skills[skill] = 1
            experience_cost = ExperienceCost(
                character_id=self.character.id, type="skill", cost=cost, name=skill
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to increase {skill} by 1"
        elif form_id == "talent_form":
            talent = captured["add_talent"]["talent"]
            cost = self.character.cost_talent(self.character.talents.get(talent, 0))
            if "(Any" in talent:
                specialisation = captured["add_talent"].get(f"{talent} specialisation")
                if "(Any)" in talent:
                    talent = talent.replace("Any", specialisation)
                else:
                    talent = talent.replace("Any Arcane Lore", specialisation)
            if captured["add_talent"]["talent"] in [
                "Chanty",
                "Petty Magic",
                "Invoke (Any)",
            ]:
                url = self.request.route_url("experience-talent", id=self.character.id)
                return f"{url}?talent={talent}"
            if talent in self.character.talents:
                self.character.talents[talent] += 1
            else:
                self.character.talents[talent] = 1
            experience_cost = ExperienceCost(
                character_id=self.character.id, type="talent", cost=cost, name=talent
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to increase {talent} by 1"
        elif form_id == "chanties_form":
            cost = self.cost_chanty()
            chanty = captured["chanties"]["chanty"]
            self.character.chanties.append(chanty)
            experience_cost = ExperienceCost(
                character_id=self.character.id,
                type="chanty",
                cost=cost,
                name=chanty,
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to learn {chanty} chanty."
        elif form_id == "magic_form":
            spell = {k: v for k, v in captured["spells"].items() if v}
            cost = self.character.spell_cost(spell)
            spell_type = list(spell.keys())[0]
            spell_name = list(spell.values())[0]
            if spell_type == "petty_magic":
                self.character.petty_magic.append(spell_name)
            elif spell_type == "arcane_magic":
                self.character.arcane_magic.append(spell_name)
            elif spell_type == "lore_magic":
                self.character.lore_magic.append(spell_name)
            experience_cost = ExperienceCost(
                character_id=self.character.id,
                type=spell_type.replace("_", " ").title(),
                cost=cost,
                name=spell_name,
            )
            spell_type_string = spell_type.replace("_", " ").title()
            self.request.dbsession.add(experience_cost)
            message = (
                f"You have spent {cost} XP to learn {spell_name} {spell_type_string} "
                "spell."
            )
        elif form_id == "miracles_form":
            cost = self.character.cost_miracle()
            miracle = captured["miracles"]["miracle"]
            self.character.miracles.append(miracle)
            experience_cost = ExperienceCost(
                character_id=self.character.id,
                type="miracle",
                cost=cost,
                name=miracle,
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to learn {miracle} miracle."
        elif form_id == "career_form":
            new_career = captured["change_career"]["advance_career"]
            self.character.career_title = new_career
            self.character.career_path.append(new_career)
            cost = 200
            if self.completed_career:
                cost = 100
            experience_cost = ExperienceCost(
                character_id=self.character.id,
                type="career",
                cost=cost,
                name=new_career,
            )
            self.request.dbsession.add(experience_cost)
            message = f"You have spent {cost} XP to advance career to {new_career}"
        self.character.experience -= cost
        self.character.experience_spent += cost
        self.request.session.flash(message, "success")
        return self.request.route_url("experience", id=self.character.id)
