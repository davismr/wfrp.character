from flask import render_template
from flask import url_for
from flask.views import MethodView
from werkzeug.routing.exceptions import RequestRedirect

from wfrp.character.database import db
from wfrp.character.models.character import Character


class CharacterView(MethodView):

    def get(self, id):
        character = db.session.query(Character).filter(Character.id == id).one()
        self.check_status(character)
        return render_template(
            "character.jinja2", title=character.get_display_title, character=character
        )

    def check_status(self, character):
        if character.status not in ["Active"]:
            expected_endpoint = f"build_{character.status.lower()}"
            redirect_url = url_for(expected_endpoint, id=character.id)
            raise RequestRedirect(redirect_url)
