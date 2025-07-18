from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.forms.create.career import CareerViews
from wfrp.character.views.homepage import HomePageViews
from wfrp.character.views.links import LinksViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.package
def test_home_view(testapp):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    view = HomePageViews(request)
    response = view.get_view()
    assert response


@pytest.mark.package
def test_home_template(testapp):
    response = testapp.get("/", status=200)
    assert "Warhammer Fantasy Roleplay Character generator" in response.ubody


@pytest.mark.package
def test_home_template_login(testapp_auth):
    response = testapp_auth.get("/", status=200)
    assert 'href="http://localhost/static/wfrp.css"/>' in response.ubody
    assert 'href="/about">About</a>' in response.ubody


@pytest.mark.package
def test_links_view():
    view = LinksViews(testing.DummyRequest())
    response = view.links_view()
    assert response == {}


@pytest.mark.package
def test_redirect_view(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    with pytest.raises(HTTPFound) as error:
        CareerViews(request)
    assert error.value.code == 302
    assert "trappings" in error.value.location
