from flask import g

from wfrp.character import __version__
from wfrp.character.forms.build.career import CareerFormView
from wfrp.character.forms.build.new import NewFormView
from wfrp.character.forms.build.species import SpeciesFormView
from wfrp.character.views.character import CharacterView
from wfrp.character.views.home import HomePageView


def register_routes(app):
    @app.before_request
    def load_request_metadata():
        g.package_version = __version__

    app.add_url_rule("/", view_func=HomePageView.as_view("homepage"))
    app.add_url_rule(
        "/character/<uuid():id>", view_func=CharacterView.as_view("character_view")
    )
    app.add_url_rule("/build/new", view_func=NewFormView.as_view("build_new"))
    app.add_url_rule(
        "/build/species/<uuid(strict=False):id>",
        view_func=SpeciesFormView.as_view("build_species"),
    )
    app.add_url_rule(
        "/build/career/<uuid(strict=False):id>",
        view_func=CareerFormView.as_view("build_career"),
    )
