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
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character_full")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.full_view()
    assert response


@pytest.mark.views
def test_summary_view(new_character):
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="character_summary")
    request.matchdict = {"uuid": new_character.uuid}
    view = CharacterViews(request)
    response = view.summary_view()
    assert "character" in response


@pytest.mark.views
@pytest.mark.skipif(
    not WEASYPRINT_INSTALLED, reason="weasyprint not installed correctly"
)
def test_pdf_view(complete_character):
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="pdf_print")
    request.matchdict = {"uuid": complete_character.uuid}
    view = CharacterViews(request)
    response = view.pdf_print()
    assert f"{complete_character.get_filename()}.pdf" in response.headers.get(
        "Content-Disposition"
    )
