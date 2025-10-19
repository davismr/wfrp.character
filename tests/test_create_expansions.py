from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.data.expansions import EXPANSIONS
from wfrp.character.views.create_character.expansions import ExpansionsViews


@dataclass
class DummyRoute:
    name: str


def all_expansions():
    expansions = {}
    for expansion in EXPANSIONS:
        expansions[expansion] = "false"
    return expansions


@pytest.mark.create
def test_get_view(new_character):
    new_character.create_data = {"expansions": ""}
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
    new_character.create_data = {"expansions": ""}
    expansions = all_expansions()
    expansions["rough_nights"] = "true"
    expansions["sea_of_claws"] = "true"
    request = testing.DummyRequest(
        post={
            "expansions": expansions,
            "Choose_Expansions": "Choose_Expansions",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert sorted(new_character.expansions) == ["rough_nights", "sea_of_claws"]


@pytest.mark.create
def test_submit_empty(new_character):
    new_character.create_data = {"expansions": ""}
    expansions = all_expansions()
    request = testing.DummyRequest(
        post={
            "expansions": expansions,
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
    new_character.create_data = {"expansions": ""}
    expansions = all_expansions()
    expansions["not_an_expansion"] = "true"
    request = testing.DummyRequest(
        post={
            "expansions": expansions,
            "Choose_Expansions": "Choose_Expansions",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="expansions")
    request.matchdict = {"id": str(new_character.id)}
    view = ExpansionsViews(request)
    response = view.form_view()
    # invalid expansions are just ignored
    assert isinstance(response, HTTPFound)
