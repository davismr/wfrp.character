from dataclasses import dataclass

from pyramid import testing
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.character import CharacterViews
from wfrp.character.views.character import WEASYPRINT_INSTALLED


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_full_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="character-full")
    request.matchdict = {"id": str(new_character.id)}
    view = CharacterViews(request)
    response = view.full_view()
    assert response


@pytest.mark.views
def test_summary_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="character-summary")
    request.matchdict = {"id": str(new_character.id)}
    view = CharacterViews(request)
    response = view.summary_view()
    assert "character" in response


@pytest.mark.views
@pytest.mark.skipif(
    not WEASYPRINT_INSTALLED, reason="weasyprint not installed correctly"
)
def test_pdf_view(complete_character):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="pdf-print")
    request.matchdict = {"id": str(complete_character.id)}
    view = CharacterViews(request)
    response = view.pdf_print()
    assert f"{complete_character.get_filename()}.pdf" in response.headers.get(
        "Content-Disposition"
    )
