from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_list import get_career
from wfrp.character.career_list import list_careers
from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.utils import roll_d100


@view_defaults(route_name="career")
class CareerViews:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET", renderer=__name__ + ":../templates/career.pt")
    def new_career_view(self):
        uuid = self.request.matchdict["uuid"]
        character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        career = get_career(character.species, roll_d100())
        career_list = list_careers(character.species)
        career_list.remove(career)
        return {"career_choice": [career], "career_list": career_list}

    @view_config(request_method="POST", renderer=__name__ + ":../templates/career.pt")
    def submit_career_view(self):
        uuid = self.request.matchdict["uuid"]
        character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        career = self.request.POST.get("career")
        if "+reroll" in career:
            career = career.replace("+reroll", "")
            career_choice = [career]
            while len(career_choice) < 3:
                career = get_career(character.species, roll_d100())
                if career not in career_choice:
                    career_choice.append(career)
            career_list = list_careers(character.species)
            for career in career_choice:
                career_list.remove(career)
            return {"career_choice": career_choice, "career_list": career_list}
        if "+50" in career:
            career = career[:-3]
            character.experience += 50
        elif "+25" in career:
            career = career[:-3]
            character.experience += 25
        character.career = career
        url = self.request.route_url("homepage")
        return HTTPFound(location=url)
