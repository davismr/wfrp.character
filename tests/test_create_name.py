from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.forms.create.name import NameViews


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
        post={"character_name": "Frodo Baggins", "Select_Name": "Select_Name"}
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"id": str(new_character.id)}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.name == "Frodo Baggins"


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
