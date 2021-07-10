from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.character import CharacterViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_full_view(new_character):
    new_character.status = {"character": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.full_view()
    assert response


@pytest.mark.views
def test_summary_view(new_character):
    new_character.status = {"character": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.summary_view()
    assert "character" in response
