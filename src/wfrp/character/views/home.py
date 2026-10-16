from flask import render_template
from flask.views import MethodView

from wfrp.character.models.character import Character


class HomePageView(MethodView):

    def get(self):
        active_characters = Character.query.filter_by(status="Active").all()
        build_characters = Character.query.filter(Character.status != "Active").all()
        return render_template(
            "home.jinja2",
            active_characters=active_characters,
            build_characters=build_characters,
        )
