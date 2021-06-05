from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.species_data import SPECIES_DATA
from wfrp.character.talents_data import get_random_talent
from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species_skills")
class SpeciesSkillsViews(BaseView):
    @view_config(
        request_method="GET", renderer=__name__ + ":../templates/species_skills.pt"
    )
    def get_view(self):
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
        return {"species_skills": species_skills, "species_talents": species_talents}

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/species_skills.pt"
    )
    def submit_view(self):
        for item in self.request.POST:
            value = self.request.POST.get(item)
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
