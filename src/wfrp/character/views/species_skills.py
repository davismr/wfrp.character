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

    @view_config(renderer=__name__ + ":../templates/species_skills.pt")
    def form_view(self):
        species = self.character.species
        species_skills = SPECIES_DATA[species]["skills"]
        species_talents = SPECIES_DATA[species]["talents"]
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
        species_skills = [(x, x) for x in species_skills]
        species_talents = [(x, x) for x in species_talents]

        class Schema(colander.Schema):
            skills_field = colander.SchemaNode(
                colander.String(),
#                default=species,
#                validator=colander.OneOf([x[0] for x in species_list]),
                widget=deform.widget.CheckboxWidget(values=species_skills),
                description=f"Select skills",
            )
            talents_field = colander.SchemaNode(
                colander.String(),
#                default=species,
                validator=colander.OneOf([x[0] for x in species_talents]),
                widget=deform.widget.RadioChoiceWidget(values=species_talents),
                description=f"Select talent",
            )

        schema = Schema()
        form = deform.Form(schema, buttons=("Choose Skills",))

        if "Choose_Skills" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:

                for item in captured:
                    value = captured.get(item)
                    if value == "on":
                        continue
                    try:
                        value = int(value)
                    except ValueError:
                        self.character.talents.append(value)
                    else:
                        self.character.skills[item] = value
                    pass
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
