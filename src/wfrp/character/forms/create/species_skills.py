import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.species import SPECIES_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.data.talents import get_random_talent
from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species_skills", permission="create_character")
class SpeciesSkillsViews(BaseView):
    def initialise_form(self):
        species = self.character.species
        species_skills = SPECIES_DATA[species]["skills"].copy()
        species_talents = SPECIES_DATA[species]["talents"].copy()
        if species in ["Human", "Halfling"]:
            if self.character.status["species_skills"]:
                extra_talents = self.character.status["species_skills"]
            else:
                extra_talents = []
                while True:
                    extra_talent = get_random_talent(roll_d100())
                    if extra_talent in extra_talents:
                        continue
                    if extra_talent in ["Savvy", "Suave"] and species == "Human":
                        continue
                    extra_talents.append(extra_talent)
                    if len(extra_talents) == 2 and species == "Halfling":
                        break
                    if len(extra_talents) == 3 and species == "Human":
                        break
                self.character.status = {"species_skills": extra_talents}
            species_talents.extend(extra_talents)
        return {"species_skills": species_skills, "species_talents": species_talents}

    def schema(self, data):
        species_skills = data["species_skills"]
        species_talents = data["species_talents"]
        schema = colander.SchemaNode(
            colander.Mapping(), title="Species Skills and Talents"
        )
        skill_schema = colander.SchemaNode(
            colander.Mapping(),
            description=(
                "You may choose 3 Skills to gain 5 Advances each, and 3 Skills to gain "
                "3 Advances each."
            ),
            validator=self.validate,
            name="species_skills",
        )
        skill_choices = ((0, "No Advances"), (3, "3 Advances"), (5, "5 Advances"))
        for skill in species_skills:
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
            if "(Any)" in skill:
                specialisation_choices = []
                choices = SKILL_DATA[skill.split(" (")[0]]["specialisations"]
                for choice in choices:
                    specialisation_choices.append((choice, choice))
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
                        name=f"Specialisation for {skill.split(' (')[0]}",
                    )
                )
        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            description=(
                "If a Talent listing presents a choice, you select one Talent from "
                "the choices given."
            ),
            name="species_talents",
        )
        for talent in species_talents:
            talent_choices = []
            for talent_choice in talent.split(" or "):
                talent_choices.append((talent_choice, talent_choice))
            talent_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=talent,
                    validator=colander.OneOf([x[0] for x in talent_choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=talent_choices, inline=True
                    ),
                    default=talent_choices[0][0],
                )
            )
        schema.add(skill_schema)
        schema.add(talent_schema)
        return schema

    def validate(self, form, values):
        errors = []
        for value in values:
            if (
                "(Any)" in value
                and values[value]
                and not values[f"Specialisation for {value.split(' (')[0]}"]
            ):
                errors.append(f"You have to select a specialisation for {value}")
        list_values = list(values.values())
        if list_values.count(3) > 3:
            errors.append("You can only select 3 skills for 3 advances")
        elif list_values.count(3) < 3:
            errors.append("You must select 3 skills for 3 advances")
        if list_values.count(5) > 3:
            errors.append("You can only select 3 skills for 5 advances")
        elif list_values.count(5) < 3:
            errors.append("You must select 3 skills for 5 advances")
        if errors:
            raise colander.Invalid(form, ". ".join(errors))

    @view_config(renderer="wfrp.character:templates/forms/skills.pt")
    def form_view(self):  # noqa: C901
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(schema, buttons=("Choose Skills",))
        if "Choose_Skills" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                for item in captured["species_skills"]:
                    value = captured["species_skills"].get(item)
                    if value == 0:
                        continue
                    if "(Any)" in item:
                        specialisation = captured["species_skills"].get(
                            f"Specialisation for {item.split(' (')[0]}"
                        )
                        self.character.skills[item.replace("Any", specialisation)] = (
                            value
                        )
                    elif "Specialisation for" not in item:
                        self.character.skills[item] = value
                for item in captured["species_talents"]:
                    value = captured["species_talents"].get(item)
                    self.character.talents[value] = 1
                url = self.request.route_url("career_skills", id=self.character.id)
                self.character.status = {"career_skills": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        form_data = {"skills": {}, "talents": {}}
        for skill in data["species_skills"]:
            if skill in SKILL_DATA:
                form_data["skills"][skill] = SKILL_DATA[skill]
            else:
                form_data["skills"][skill] = SKILL_DATA[skill.split(" (")[0]]
        for talent in data["species_talents"]:
            if talent in TALENT_DATA:
                form_data["talents"][talent] = TALENT_DATA[talent]
            elif " or " in talent:
                for talent in talent.split(" or "):
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
