from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="career_skills")
class CareerSkillsViews(BaseView):
    @view_config(
        request_method="GET", renderer=__name__ + ":../templates/career_skills.pt"
    )
    def get_view(self):
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_skills = career_details["skills"]
        career_talents = career_details["talents"]
        return {"career_skills": career_skills, "career_talents": career_talents}

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/career_skills.pt"
    )
    def submit_view(self):
        url = self.request.route_url("trappings", uuid=self.character.uuid)
        self.character.status = {"trappings": ""}
        return HTTPFound(location=url)
