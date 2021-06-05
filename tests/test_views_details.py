from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.details import DetailsViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_details_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"details": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="details")
    request.matchdict = {"uuid": new_character.uuid}
    view = DetailsViews(request)
    response = view.get_view()
    assert "age" in response
    assert "height" in response
    assert "hair_colour" in response
    assert "eye_colour" in response
    assert len(response["eye_colour"].split(","))
