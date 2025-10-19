from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.experience_talent import ExperienceTalentViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_form_view(complete_character):
    complete_character.species = "High Elf"
    complete_character.career = "Wizard"
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(complete_character.id)}
    request.GET = {"talent": "Petty Magic"}
    view = ExperienceTalentViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)
    assert "Marsh Lights" in response["form"]


@pytest.mark.views
def test_submit(complete_character):
    complete_character.species = "High Elf"
    complete_character.career = "Wizard"
    complete_character.willpower_initial = 34
    request = testing.DummyRequest(
        post={
            "spells": {"Animal Friend": "true", "Gust": "true", "Rot": "true"},
            "Choose_Spells": "Choose_Spells",
        }
    )
    request.GET = {"talent": "Petty Magic"}
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience-talent")
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceTalentViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert complete_character.petty_magic == ["Animal Friend", "Gust", "Rot"]
