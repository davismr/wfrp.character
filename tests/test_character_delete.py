from pyramid import testing
import pytest

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.character import Character
from wfrp.character.models.experience import ExperienceCost
from wfrp.character.models.experience import ExperienceGain
from wfrp.character.models.user import User
from wfrp.character.views.transfer_character import TransferViews


@pytest.mark.character
def test_character_delete(new_character):
    experience_cost = ExperienceCost(
        character_id=new_character.id,
        type="characteristic",
        cost=10,
        name="Intelligence",
    )
    DBSession.add(experience_cost)
    assert DBSession.query(ExperienceCost).count() == 1
    experience_gain = ExperienceGain(
        character_id=new_character.id,
        amount=1000,
        reason="Free experience",
    )
    DBSession.add(experience_gain)
    assert DBSession.query(ExperienceGain).count() == 1
    request = testing.DummyRequest(
        post={"confirm_delete": "true", "Confirm_Delete": "Confirm_Delete"}
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = TransferViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    assert DBSession.query(Character).all() == []
    assert DBSession.query(ExperienceCost).all() == []
    assert DBSession.query(ExperienceGain).all() == []


@pytest.mark.character
def test_character_transfer(new_character):
    old_user = User()
    old_user.name = "User from transfer"
    DBSession.add(old_user)
    old_user = DBSession.query(User).filter_by(name="User from transfer").first()
    new_character.user_id = old_user.id
    assert new_character.user == old_user
    new_user = User()
    new_user.name = "User to transfer"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(name="User to transfer").first()
    request = testing.DummyRequest(
        post={
            "transfer_character": {"transfer_user": str(new_user.id)},
            "confirm_transfer": "true",
            "Confirm_Transfer": "Confirm_Transfer",
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = TransferViews(request)
    response = view.post_view()
    assert response.status_code == 302
    assert response.location == "/"
    assert new_character.user_id == new_user.id
