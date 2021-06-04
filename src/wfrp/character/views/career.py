from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import get_career
from wfrp.character.career_data import list_careers
from wfrp.character.utils import roll_d100
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="career")
class CareerViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/career.pt")
    def new_career_view(self):
        if self.character.status["career"]:
            career = self.character.status["career"]
        else:
            career = get_career(self.character.species, roll_d100())
            self.character.status = {"career": career}
        career_list = list_careers(self.character.species)
        career_list.remove(career)
        return {"career_choice": [career], "career_list": career_list}

    @view_config(
        request_method="POST",
        request_param="form.reroll",
        renderer=__name__ + ":../templates/career.pt",
    )
    def reroll_career_view(self):
        career_choice = self.character.status["career"].split(",")
        while len(career_choice) < 3:
            career = get_career(self.character.species, roll_d100())
            if career not in career_choice:
                career_choice.append(career)
        self.character.status = {"career": ",".join(career_choice)}
        career_list = list_careers(self.character.species)
        for career in career_choice:
            career_list.remove(career)
        return {"career_choice": career_choice, "career_list": career_list}

    @view_config(request_method="POST", renderer=__name__ + ":../templates/career.pt")
    def submit_career_view(self):
        career = self.request.POST.get("career")
        career_choice = self.character.status["career"].split(",")
        if career in career_choice:
            if len(career_choice) == 1:
                self.character.experience += 50
            else:
                self.character.experience += 25
        self.character.career = career
        url = self.request.route_url("attributes", uuid=self.character.uuid)
        self.character.status = {"attributes": ""}
        return HTTPFound(location=url)
