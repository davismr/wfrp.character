from datetime import datetime
from datetime import timezone

from freezegun import freeze_time

from wfrp.character.database import db
from wfrp.character.models.user import User


def test_user():
    user = User(given_name="A", family_name="User", email="user@here.com")
    assert user.given_name == "A"
    assert user.family_name == "User"
    assert user.email == "user@here.com"


def test_modified(client):
    new_user = User()
    new_user.name = "A new User"
    with freeze_time("2024-01-02 03:04:05"):
        db.session.add(new_user)
        new_user = db.session.query(User).filter_by(name="A new User").first()
    assert new_user.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_user.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_user.name = "A newer User"
        new_user = db.session.query(User).filter_by(name="A newer User").first()
    assert new_user.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)


def test_character_relationship(new_character):
    new_user = User()
    new_user.name = "User with Character"
    db.session.add(new_user)
    new_user = db.session.query(User).filter_by(name="User with Character").first()
    new_character.user_id = new_user.id
    assert new_character.user == new_user
    assert len(new_user.characters) == 1
    assert new_user.characters[0] == new_character
