from flask import render_template
from flask.views import MethodView

from wfrp.character.models.character import Character


class HomePageView(MethodView):

    def get(self):
        all_characters = Character.query.all()
        return render_template("home.jinja2", title="Home", characters=all_characters)
