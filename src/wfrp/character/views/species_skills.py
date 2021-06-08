import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.species_data import SPECIES_DATA
from wfrp.character.talents_data import get_random_talent
from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species_skills")
class SpeciesSkillsViews(BaseView):
    def validate_advances(self, form, value):
        errors = []
        list_values = list(value.values())
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

    @view_config(renderer=__name__ + ":../templates/species_skills.pt")
    def form_view(self):
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

        schema = colander.SchemaNode(
            colander.Mapping(), title="Species Skills and Talents"
        )
        skill_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Species Skills",
            description=(
                "You may choose 3 Skills to gain 5 Advances each, and 3 Skills to gain "
                "3 Advances each."
            ),
            validator=self.validate_advances,
            name="species_skills",
        )
        skill_choices = ((5, "5 Advances"), (3, "3 Advances"), (0, "No Advances"))
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

        talent_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Species Talents",
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
                    validator=colander.OneOf([x[0] for x in talent_choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=talent_choices, inline=True
                    ),
                    default=talent_choices[0][0],
                    name=talent,
                )
            )
        schema.add(skill_schema)
        schema.add(talent_schema)
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
                    self.character.skills[item] = value
                for item in captured["species_talents"]:
                    value = captured["species_talents"].get(item)
                    self.character.talents.append(value)
                url = self.request.route_url("career_skills", uuid=self.character.uuid)
                self.character.status = {"career_skills": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
