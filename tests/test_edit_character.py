from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.application import dbsession
from wfrp.character.forms.create.name import NameViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.edit
def test_form_view(new_character):
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="character_edit")
    request.matchdict = {"uuid": new_character.uuid}
    view = NameViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
