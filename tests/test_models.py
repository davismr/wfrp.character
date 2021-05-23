import pytest

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@pytest.mark.models
def test_save_character(session_db):
    new_character = Character()
    new_character.name = "Jacob Grimm"
    assert new_character.name == "Jacob Grimm"
    DBSession.add(new_character)
    assert DBSession.query(Character).count() == 1
    character = DBSession.query(Character).order_by(Character.uid).first()
    assert character.uid == 1
    assert character.name == "Jacob Grimm"
