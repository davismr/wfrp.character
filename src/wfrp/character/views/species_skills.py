from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.species_data import SPECIES_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species_skills")
class SpeciesSkillsViews(BaseView):
    @view_config(
        request_method="GET", renderer=__name__ + ":../templates/species_skills.pt"
    )
    def get_view(self):
        species_skills = SPECIES_DATA[self.character.species]["skills"]
        species_talents = SPECIES_DATA[self.character.species]["talents"]
        # TODO random talents
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
