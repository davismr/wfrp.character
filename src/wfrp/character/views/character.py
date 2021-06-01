from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="character")
class CharacterViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/character.pt")
    def character_get_view(self):
        return {"character": self.character}
