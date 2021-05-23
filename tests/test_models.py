import pytest
import transaction

from wfrp.character.models import Character
from wfrp.character.models import DBSession


@pytest.mark.models
def test_save_character(session_db):
    new_character = Character()
    new_character.name = "James Stuart"
    assert new_character.name == "James Stuart"
    DBSession.add(new_character)
    transaction.commit()
    assert DBSession.query(Character).count() == 1
    character = DBSession.query(Character).order_by(Character.uid).first()
    assert character.uid == 1
    assert character.name == "James Stuart"
