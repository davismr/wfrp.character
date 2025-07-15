from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.character import Character


@view_defaults(route_name="account")
class AccountPageViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(request_method="GET", renderer="wfrp.character:templates/account.pt")
    def get_view(self):
        characters = self.request.dbsession.query(Character).all()
        character_list = {}
        for character in characters:
            url = self.request.route_url("character_summary", id=character.id)
            character_list[url] = character.get_display_title()
        return {"characters": character_list}
