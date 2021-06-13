from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@view_defaults(route_name="homepage")
class HomePageViews:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET", renderer="wfrp.character:templates/homepage.pt")
    def get_view(self):
        characters = DBSession.query(Character).all()
        character_list = {}
        for character in characters:
            url = self.request.route_url("character", uuid=character.uuid)
            character_list[url] = character.get_display_title()
        return {"characters": character_list}
