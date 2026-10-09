from flask import render_template
from flask.views import MethodView

from wfrp.character.database import db
from wfrp.character.models.character import Character


class CharacterView(MethodView):

    def get(self, id):
        character = db.session.query(Character).filter(Character.id == id).one()
        return render_template(
            "character.jinja2", title=character.get_display_title, character=character
        )
