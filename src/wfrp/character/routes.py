from flask import current_app
from flask import g

from wfrp.character import __version__
from wfrp.character.views.character import CharacterView
from wfrp.character.views.home import HomePageView


@current_app.before_request
def load_request_metadata():
    g.package_version = __version__


current_app.add_url_rule("/", view_func=HomePageView.as_view("Home"))
current_app.add_url_rule(
    "/character/<uuid():id>", view_func=CharacterView.as_view("CharacterView")
)
