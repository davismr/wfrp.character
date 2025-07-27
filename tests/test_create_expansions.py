from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.expansions import ExpansionsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_get_view(new_character):
    new_character.status = {"expansions": ""}
    request = testing.DummyRequest(path="expansions")
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    assert "form" in response
    assert "Rough Nights and Hard Days" in response["form"]
    assert "Choose expansions" in response["form"]


@pytest.mark.create
def test_submit_view(new_character):
    new_character.status = {"expansions": ""}
    request = testing.DummyRequest(
        post={
            "expansions": {"expansions": ["rough_nights", "up_in_arms"]},
            "Choose_Expansions": "Choose_Expansions",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert sorted(new_character.expansions) == ["rough_nights", "up_in_arms"]


@pytest.mark.create
def test_submit_empty(new_character):
    new_character.status = {"expansions": ""}
    request = testing.DummyRequest(
        post={
            "expansions": {"expansions": []},
            "Choose_Expansions": "Choose_Expansions",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.expansions == []


@pytest.mark.create
def test_submit_invalid_expansion(new_character):
    new_character.status = {"expansions": ""}
    request = testing.DummyRequest(
        post={
            "expansions": {"expansions": ["not_an_expansion", "up_in_arms"]},
            "Choose_Expansions": "Choose_Expansions",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "One or more of the choices you made was not acceptable" in response["form"]
