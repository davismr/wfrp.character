from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
import transaction

from pyramid.httpexceptions import HTTPCreated

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@view_defaults(route_name="new_character")
class NewCharacterViews:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def character_get_view(self):
        response = HTTPCreated()
        new_character = Character()
        DBSession.add(new_character)
        transaction.commit()
        import pdb;pdb.set_trace()
        url = self.request.route_url("species", uuid=new_character.uuid)
        response.location = self.request.resource_url(url)
        return response


#        result = render(__name__ + ":../templates/species.pt", {}, request=self.request)
#        return Response(result)

#    @view_config(request_method="POST")
#    def character_post_view(self):
#        character = Character(name=self.request.params["name"])
#        DBSession.add(character)
#        # XXX should automatically commit on success
#        transaction.commit()
#        character = DBSession.query(Character).order_by(Character.uid).first()
#        new_uuid = character.uuid
#        url = self.request.route_url("attributes", uuid=new_uuid)
#        return HTTPFound(url)
