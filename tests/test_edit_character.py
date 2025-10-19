from dataclasses import dataclass

from pyramid import testing
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.name import NameViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.edit
def test_form_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="character-edit")
    request.matchdict = {"id": str(new_character.id)}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
