from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_list import get_career
from wfrp.character.career_list import list_careers
from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.utils import roll_2d10


@view_defaults(route_name="attributes")
class CareerViews:
    def __init__(self, request):
        self.request = request

    def _get_base_attributes(self, species):
        attributes = {
            "Weapon Skill": roll_2d10() + 20,
            "Ballistic Skill": roll_2d10() + 20,
            "Strength": roll_2d10() + 20,
            "Toughness": roll_2d10() + 20,
            "Initiative": roll_2d10() + 20,
            "Agility": roll_2d10() + 20,
            "Dexterity": roll_2d10() + 20,
            "Intelligence": roll_2d10() + 20,
            "Willpower": roll_2d10() + 20,
            "Fellowship": roll_2d10() + 20,
        }
        return {"attributes": attributes}

    @view_config(request_method="GET", renderer=__name__ + ":../templates/attributes.pt")
    def new_career_view(self):
        uuid = self.request.matchdict["uuid"]
        character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        attributes = self._get_base_attributes(character.species)
        return attributes

    @view_config(request_method="POST", renderer=__name__ + ":../templates/attributes.pt")
    def submit_career_view(self):
        uuid = self.request.matchdict["uuid"]
        character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        url = self.request.route_url("homepage")
        return HTTPFound(location=url)
