from wfrp.character.models import Character
from wfrp.character.models import DBSession


class BaseView:
    def __init__(self, request):
        self.request = request
        uuid = request.matchdict["uuid"]
        self.character = DBSession.query(Character).filter(Character.uuid == uuid).one()
