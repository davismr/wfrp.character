from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.name import NameViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_get_view(new_character):
    new_character.status = {"name": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"id": str(new_character.id)}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.create
def test_submit_view(new_character):
    new_character.status = {"name": ""}
    request = testing.DummyRequest(
        post={
            "character_name": "Frodo Baggins",
            "Select_Name": "Select_Name",
            "ambition": {
                "long_term_ambition": "Destroy the ring",
                "short_term_ambition": "Reach Bree",
            },
            "motivation": {"motivation": "Keep going"},
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"id": str(new_character.id)}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.name == "Frodo Baggins"
    assert new_character.motivation == "Keep going"
    assert new_character.short_term_ambition == "Reach Bree"
    assert new_character.long_term_ambition == "Destroy the ring"


@pytest.mark.create
def test_submit_invalid(new_character):
    new_character.status = {"name": ""}
    request = testing.DummyRequest(
        post={"character_name": "a" * 101, "Select_Name": "Select_Name"}
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"id": str(new_character.id)}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "Longer than maximum length 100" in response["form"]
