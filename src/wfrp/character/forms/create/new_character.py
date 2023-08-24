import uuid

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@view_defaults(route_name="new_character")
class NewCharacterViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(request_method="GET")
    def get_view(self):
        new_uuid = str(uuid.uuid4())
        new_character = Character(uuid=new_uuid)
        DBSession.add(new_character)
        url = self.request.route_url("species", uuid=new_uuid)
        new_character.status = {"species": ""}
        return HTTPFound(location=url)
