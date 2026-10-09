from datetime import datetime
from datetime import timezone

from freezegun import freeze_time

from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_save_character(client):
    # make sure db is empty
    db.session.query(Character).delete()
    new_character = Character()
    new_character.name = "Jacob Grimm"
    assert new_character.name == "Jacob Grimm"
    db.session.add(new_character)
    assert db.session.query(Character).count() == 1
    character = db.session.query(Character).first()
    assert character.name == "Jacob Grimm"


def test_modified(client):
    # make sure db is empty
    db.session.query(Character).delete()
    new_character = Character()
    new_character.name = "Wilhelm Grimm"
    with freeze_time("2024-01-02 03:04:05"):
        db.session.add(new_character)
        new_charcter = (
            db.session.query(Character).filter_by(name="Wilhelm Grimm").first()
        )
    assert new_charcter.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_charcter.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_character.name = "Jacob Grimm"
        new_charcter = db.session.query(Character).filter_by(name="Jacob Grimm").first()
    assert new_charcter.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)


def test_toughness(new_character):
    new_character.species = "Human"
    new_character.toughness_initial = 36
    new_character.toughness_advances = 5
    assert new_character.toughness == 41
    new_character.talents = {"Very Resilient": 1}
    assert new_character.toughness == 46
