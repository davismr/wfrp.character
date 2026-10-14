from flask import g

from wfrp.character import __version__
from wfrp.character.forms.build.career import CareerFormView
from wfrp.character.forms.build.characteristics import CharacteristicsFormView
from wfrp.character.forms.build.magic import MagicFormView
from wfrp.character.forms.build.name import NameFormView
from wfrp.character.forms.build.new import NewFormView
from wfrp.character.forms.build.physical import PhysicalFormView
from wfrp.character.forms.build.religion import ReligionFormView
from wfrp.character.forms.build.skills import SkillsFormView
from wfrp.character.forms.build.species import SpeciesFormView
from wfrp.character.forms.build.talents import TalentsFormView
from wfrp.character.forms.build.trappings import TrappingsFormView
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
        "/build/physical/<uuid(strict=False):id>",
        view_func=PhysicalFormView.as_view("build_physical"),
    )
    app.add_url_rule(
        "/build/career/<uuid(strict=False):id>",
        view_func=CareerFormView.as_view("build_career"),
    )
    app.add_url_rule(
        "/build/religion/<uuid(strict=False):id>",
        view_func=ReligionFormView.as_view("build_religion"),
    )
    app.add_url_rule(
        "/build/characteristics/<uuid(strict=False):id>",
        view_func=CharacteristicsFormView.as_view("build_characteristics"),
    )
    app.add_url_rule(
        "/build/skills/<uuid(strict=False):id>",
        view_func=SkillsFormView.as_view("build_skills"),
    )
    app.add_url_rule(
        "/build/talents/<uuid(strict=False):id>",
        view_func=TalentsFormView.as_view("build_talents"),
    )
    app.add_url_rule(
        "/build/magic/<uuid(strict=False):id>",
        view_func=MagicFormView.as_view("build_magic"),
    )
    app.add_url_rule(
        "/build/trappings/<uuid(strict=False):id>",
        view_func=TrappingsFormView.as_view("build_trappings"),
    )
    app.add_url_rule(
        "/build/name/<uuid(strict=False):id>",
        view_func=NameFormView.as_view("build_name"),
    )
