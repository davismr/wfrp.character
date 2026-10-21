from flask import g

from wfrp.character import __version__
from wfrp.character.forms.create.career import CareerFormView
from wfrp.character.forms.create.characteristics import CharacteristicsFormView
from wfrp.character.forms.create.magic import MagicFormView
from wfrp.character.forms.create.name import NameFormView
from wfrp.character.forms.create.new import NewFormView
from wfrp.character.forms.create.physical import PhysicalFormView
from wfrp.character.forms.create.religion import ReligionFormView
from wfrp.character.forms.create.skills import SkillsFormView
from wfrp.character.forms.create.species import SpeciesFormView
from wfrp.character.forms.create.talents import TalentsFormView
from wfrp.character.forms.create.trappings import TrappingsFormView
from wfrp.character.views.character import CharacterSheetView
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
    app.add_url_rule(
        "/character-sheet/<uuid():id>",
        view_func=CharacterSheetView.as_view("character_sheet_view"),
    )
    app.add_url_rule("/create/new", view_func=NewFormView.as_view("create_new"))
    app.add_url_rule(
        "/create/species/<uuid(strict=False):id>",
        view_func=SpeciesFormView.as_view("create_species"),
    )
    app.add_url_rule(
        "/create/physical/<uuid(strict=False):id>",
        view_func=PhysicalFormView.as_view("create_physical"),
    )
    app.add_url_rule(
        "/create/career/<uuid(strict=False):id>",
        view_func=CareerFormView.as_view("create_career"),
    )
    app.add_url_rule(
        "/create/religion/<uuid(strict=False):id>",
        view_func=ReligionFormView.as_view("create_religion"),
    )
    app.add_url_rule(
        "/create/characteristics/<uuid(strict=False):id>",
        view_func=CharacteristicsFormView.as_view("create_characteristics"),
    )
    app.add_url_rule(
        "/create/skills/<uuid(strict=False):id>",
        view_func=SkillsFormView.as_view("create_skills"),
    )
    app.add_url_rule(
        "/create/talents/<uuid(strict=False):id>",
        view_func=TalentsFormView.as_view("create_talents"),
    )
    app.add_url_rule(
        "/create/magic/<uuid(strict=False):id>",
        view_func=MagicFormView.as_view("create_magic"),
    )
    app.add_url_rule(
        "/create/trappings/<uuid(strict=False):id>",
        view_func=TrappingsFormView.as_view("create_trappings"),
    )
    app.add_url_rule(
        "/create/name/<uuid(strict=False):id>",
        view_func=NameFormView.as_view("create_name"),
    )
