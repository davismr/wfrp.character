from datetime import datetime
from datetime import timezone

import pytest
from freezegun import freeze_time

from wfrp.character.application import DBSession
from wfrp.character.models.user import User


@pytest.mark.models
def test_add_user(testapp):
    # make sure db is empty
    DBSession.query(User).delete()
    new_user = User()
    new_user.name = "A User"
    new_user.email = "user@here.com"
    new_user.password = "secret_password"
    DBSession.add(new_user)
    assert DBSession.query(User).count() == 1
    user = DBSession.query(User).first()
    assert user.name == "A User"
    assert user.email == "user@here.com"
    assert user.password == "secret_password"
    DBSession.query(User).delete()


@pytest.mark.models
def test_modified(testapp):
    new_user = User()
    new_user.name = "A new User"
    with freeze_time("2024-01-02 03:04:05"):
        DBSession.add(new_user)
        new_user = DBSession.query(User).filter_by(name="A new User").first()
    assert new_user.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_user.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_user.name = "A newer User"
        new_user = DBSession.query(User).filter_by(name="A newer User").first()
    assert new_user.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)
