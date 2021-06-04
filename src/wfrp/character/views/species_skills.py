from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.species_list import SPECIES_LIST
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="species_skills")
class SpeciesSkillsViews(BaseView):
    @view_config(
        request_method="GET", renderer=__name__ + ":../templates/species_skills.pt"
    )
    def get_view(self):
        species_skills = SPECIES_LIST[self.character.species]["skills"]
        species_talents = SPECIES_LIST[self.character.species]["talents"]
        return {"species_skills": species_skills, "species_talents": species_talents}

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/species_skills.pt"
    )
    def submit_view(self):
        url = self.request.route_url("career_skills", uuid=self.character.uuid)
        self.character.status = {"career_skills": ""}
        return HTTPFound(location=url)
