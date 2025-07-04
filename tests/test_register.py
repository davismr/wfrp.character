import pytest
from pyramid.httpexceptions import HTTPUnauthorized

from wfrp.character.application import DBSession
from wfrp.character.models.character import Character
from wfrp.character.models.user import User


@pytest.mark.register
def test_register(testapp_auth):
    payload = {
        "name": "User Name",
        "email": "user@here.com",
        "password": "a_password",
        "form.submitted": "Register",
    }
    testapp_auth.post("/register", payload, status=302)
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
    testapp_auth.post("/login", payload, status=302)
    character_count = DBSession.query(Character).count()
    testapp_auth.get("/character/new", status=302)
    assert DBSession.query(Character).count() == character_count + 1
    testapp_auth.get("/logout", status=302)
    with pytest.raises(HTTPUnauthorized) as error:
        testapp_auth.get("/character/new")
    assert str(error.value) == (
        "This server could not verify that you are authorized to access the document "
        "you requested.  Either you supplied the wrong credentials (e.g., "
        "bad password), or your browser does not understand how to supply the "
        "credentials required."
    )
