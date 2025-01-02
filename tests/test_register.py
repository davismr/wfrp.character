import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import DBSession
from wfrp.character.models.user import User
from wfrp.character.views.auth import AuthViews


@pytest.mark.register
def test_register(testapp):
    payload = {
        "name": "User Name",
        "email": "user@here.com",
        "password": "a_password",
        "form.submitted": "Register",
    }
    request = testing.DummyRequest(post=payload)
    response = AuthViews(request).register()
    assert isinstance(response, HTTPFound)
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
    request = testing.DummyRequest(post=payload)
    response = AuthViews(request).login()
    assert isinstance(response, HTTPFound)
