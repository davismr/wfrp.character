from pyramid import testing
import pytest

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.character import Character
from wfrp.character.models.user import User
from wfrp.character.views.account import AccountPageViews


@pytest.mark.account
def test_account_delete(new_character):
    DBSession.query(User).delete()
    DBSession.query(Character).delete()
    new_user = User()
    new_user.name = "User to Delete"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(name="User to Delete").first()
    new_character.user_id = new_user.id
    assert new_character.user == new_user
    request = testing.DummyRequest(
        post={
            "confirm_delete": "true",
            "Confirm_Delete_Account": "Confirm_Delete_Account",
        }
    )
    request.dbsession = dbsession(request)
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    assert DBSession.query(User).all() == []
    assert DBSession.query(Character).all() == []


@pytest.mark.account
def test_account_update():
    DBSession.query(User).delete()
    new_user = User()
    new_user.name = "User to Update"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(name="User to Update").first()
    assert new_user.subscribed is False
    request = testing.DummyRequest(post={"Update_Account": "Update_Account"})
    request.dbsession = dbsession(request)
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    new_user = DBSession.query(User).filter_by(name="User to Update").first()
    assert new_user.subscribed is False


@pytest.mark.account
def test_account_subscribe():
    DBSession.query(User).delete()
    new_user = User()
    new_user.name = "User to Subscribe"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(name="User to Subscribe").first()
    assert new_user.subscribed is False
    request = testing.DummyRequest(
        post={"Subscribe": "true", "Update_Account": "Update_Account"}
    )
    request.dbsession = dbsession(request)
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    new_user = DBSession.query(User).filter_by(name="User to Subscribe").first()
    assert new_user.subscribed is True
