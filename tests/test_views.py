import pytest
from pyramid import testing

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.views.character import NewCharacterViews
from wfrp.character.views.species import SpeciesViews


@pytest.mark.views
def test_passing_view(session_db):
    view = NewCharacterViews(testing.DummyRequest())
    response = view.character_get_view()
    assert response.status_code == 302
    assert "Location" in response.headers


@pytest.mark.views
def test_species_view(session_db):
    new_character = Character()
    DBSession.add(new_character)
    view = SpeciesViews(testing.DummyRequest())
    response = view.new_species_view()
    assert "result" in response
    assert "species_list" in response
    assert response["result"] not in response["species_list"]
