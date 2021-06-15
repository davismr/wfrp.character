from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.skill_data import SKILL_DATA
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="character")
class CharacterViews(BaseView):
    @view_config(request_method="GET", renderer="wfrp.character:templates/character.pt")
    def get_view(self):
        return {"character": self.character, "skill_data": SKILL_DATA}
