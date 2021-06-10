from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.name import NameViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.status = {"name": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"uuid": new_character.uuid}
    view = NameViews(request)
    response = view.form_view()
    assert "form" in response


@pytest.mark.views
def test_submit_view(new_character):
    new_character.status = {"name": ""}
    request = testing.DummyRequest(
        post={"character_name": "Frodo Baggins", "Select_Name": "Select_Name"}
    )
    request.matched_route = DummyRoute(name="name")
    request.matchdict = {"uuid": new_character.uuid}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.name == "Frodo Baggins"
