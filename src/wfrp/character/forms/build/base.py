from flask.views import MethodView

from wfrp.character.database import db
from wfrp.character.models.character import Character


class BaseBuildForm(MethodView):

    def get_character(self, id):
        self.character = db.session.query(Character).filter(Character.id == id).one()
