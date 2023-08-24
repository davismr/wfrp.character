from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.forms.create.career import CareerViews
from wfrp.character.views.homepage import HomePageViews
from wfrp.character.views.links import LinksViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.package
def test_home_view():
    view = HomePageViews(testing.DummyRequest())
    response = view.get_view()
    assert response


@pytest.mark.current
def test_home_template(testapp):
    response = testapp.get("/", status=200)
    assert 'href="http://localhost/login">Log In</a>' in response.ubody


@pytest.mark.package
def test_links_view():
    view = LinksViews(testing.DummyRequest())
    response = view.links_view()
    assert response == {}


@pytest.mark.package
def test_redirect_view(new_character):
    new_character.status = {"trappings": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    with pytest.raises(HTTPFound) as error:
        CareerViews(request)
    assert error.value.code == 302
    assert "trappings" in error.value.location
