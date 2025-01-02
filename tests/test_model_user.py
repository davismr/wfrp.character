import pytest

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
    assert user.uid == 1
    assert user.name == "A User"
    assert user.email == "user@here.com"
    assert user.password == "secret_password"
    DBSession.query(User).delete()
