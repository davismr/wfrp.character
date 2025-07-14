import pytest
from pyramid import testing

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.user import User
from wfrp.character.views.auth import AuthViews


@pytest.mark.register
def test_register(testapp_auth):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.session["user"] = {
        "email": "user@here.com",
        "name": "User Name",
        "given_name": "GivenName",
        "family_name": "FamilyName",
    }
    "form.submitted" in request.POST
    request.POST["form.submitted"] = "register"
    view = AuthViews(request)
    response = view.register()
    assert response.status_code == 302
    assert response.location == "http://example.com/"
    user = DBSession.query(User).filter_by(name="User Name").first()
    assert user.name == "User Name"
    assert user.email == "user@here.com"
    assert user.given_name == "GivenName"
    assert user.family_name == "FamilyName"
