from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.career import CareerViews
from wfrp.character.views.homepage import HomePageViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.package
def test_passing_view(session_db):
    view = HomePageViews(testing.DummyRequest())
    response = view.get_view()
    assert response


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
