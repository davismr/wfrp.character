import pytest
from pyramid.httpexceptions import HTTPForbidden

from wfrp.character.application import DBSession
from wfrp.character.models.character import Character
from wfrp.character.models.user import User


@pytest.mark.register
def test_register(testapp):
    payload = {
        "name": "User Name",
        "email": "user@here.com",
        "password": "a_password",
        "form.submitted": "Register",
    }
    testapp.post("/register", payload, status=302)
    users = DBSession.query(User).all()
    assert len(users) == 1
    user = users[0]
    assert user.name == "User Name"
    assert user.email == "user@here.com"
    payload = {
        "login": "user@here.com",
        "password": "a_password",
        "form.submitted": "Log In",
    }
    testapp.post("/login", payload, status=302)
    character_count = DBSession.query(Character).count()
    testapp.get("/character/new", status=302)
    assert DBSession.query(Character).count() == character_count + 1
    testapp.get("/logout", status=302)
    with pytest.raises(HTTPForbidden) as error:
        testapp.get("/character/new")
    assert str(error.value) == "Unauthorized: NewCharacterViews failed permission check"
