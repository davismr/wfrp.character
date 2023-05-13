from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.character import WEASYPRINT_INSTALLED
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


def mock_static_url(static_path):
    return "not_a_path"


@pytest.mark.views
@pytest.mark.skipif(
    not WEASYPRINT_INSTALLED, reason="weasyprint not installed correctly"
)
def test_pdf_view(new_character):
    new_character.status = {"character": ""}
    # TODO need a fully created character
    new_character.height = 66
    request = testing.DummyRequest()
    # TODO fix crude mock method
    request.static_url = mock_static_url
    request.matched_route = DummyRoute(name="character")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.pdf_print()
    # TODO fix headers
    assert "example.pdf" in response.headers.get("Content-Disposition")
