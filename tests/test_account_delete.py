import uuid

from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.testing import DummyRequest
import pytest
from sqlalchemy.exc import NoResultFound

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.character import Character
from wfrp.character.models.user import User
from wfrp.character.views.account import AccountPageViews


@pytest.mark.account
def test_account_delete(dummy_config):
    DBSession.query(User).delete()
    DBSession.query(Character).delete()
    new_user = User()
    new_user.name = "User to Delete"
    new_user.email = "delete@me.com"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(name="User to Delete").first()
    new_id = uuid.uuid4()
    new_character = Character(
        id=new_id, user_id=new_user.id, create_data={"campaign": ""}
    )
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.id == new_id).one()
    assert character.user == new_user
    assert character.user == new_user
    request = DummyRequest(
        post={
            "confirm_delete": "true",
            "Confirm_Delete_Account": "Confirm_Delete_Account",
        }
    )
    request.dbsession = dbsession(request)
    with pytest.raises(HTTPUnauthorized):
        AccountPageViews(request)
    dummy_config.testing_securitypolicy(userid="delete@me.com")
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    assert DBSession.query(User).all() == []
    assert DBSession.query(Character).all() == []
    with pytest.raises(NoResultFound):
        DBSession.query(Character).filter(Character.id == new_id).one()


@pytest.mark.account
def test_account_update(dummy_config):
    DBSession.query(User).delete()
    new_user = User()
    new_user.email = "update@me.com"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(email="update@me.com").first()
    assert new_user.subscribed is False
    request = DummyRequest(post={"Update_Account": "Update_Account"})
    request.dbsession = dbsession(request)
    dummy_config.testing_securitypolicy(userid="update@me.com")
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    new_user = DBSession.query(User).filter_by(email="update@me.com").first()
    assert new_user.subscribed is False


@pytest.mark.account
def test_account_subscribe(dummy_config):
    DBSession.query(User).delete()
    new_user = User()
    new_user.email = "subscribe@me.com"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(email="subscribe@me.com").first()
    assert new_user.subscribed is False
    request = DummyRequest(
        post={"Subscribe": "true", "Update_Account": "Update_Account"}
    )
    request.dbsession = dbsession(request)
    dummy_config.testing_securitypolicy(userid="subscribe@me.com")
    view = AccountPageViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    new_user = DBSession.query(User).filter_by(email="subscribe@me.com").first()
    assert new_user.subscribed is True
