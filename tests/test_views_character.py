from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.character import CharacterViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.status = {"character": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.get_view()
    assert response
