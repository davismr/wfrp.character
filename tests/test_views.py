import pytest
from pyramid import testing

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.views.character import NewCharacterViews
from wfrp.character.views.species import SpeciesViews


@pytest.mark.current
def test_passing_view(session_db):
    view = NewCharacterViews(testing.DummyRequest())
    response = view.character_get_view()
    import pdb;pdb.set_trace()
    assert response.status_code == 200
    assert "<h2>Character name</h2>" in response.text


@pytest.mark.skip
def test_new_view(session_db):
    view = SpeciesViews(testing.DummyRequest())
    import pdb;pdb.set_trace()
    response = view.new_species_view()
    assert response.status_code == 200
    assert "<h2>Character name</h2>" in response.text


@pytest.mark.views
def test_species_view(session_db):
    new_character = Character()
    DBSession.add(new_character)
    view = SpeciesViews(testing.DummyRequest())
    import pdb;pdb.set_trace()
    response = view.new_species_view()
    assert response.status_code == 200
    assert "<h2>Character name</h2>" in response.text
