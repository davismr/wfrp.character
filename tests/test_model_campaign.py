from datetime import datetime
from datetime import timezone

import pytest
from freezegun import freeze_time

from wfrp.character.application import DBSession
from wfrp.character.models.campaign import Campaign
from wfrp.character.models.user import User


@pytest.mark.models
def test_add_campaign(testapp):
    # make sure db is empty
    DBSession.query(Campaign).delete()
    new_campaign = Campaign()
    new_campaign.name = "My Campaign"
    new_campaign.expansions = ["rough_nights", "up_in_arms"]
    DBSession.add(new_campaign)
    assert DBSession.query(Campaign).count() == 1
    campaign = DBSession.query(Campaign).first()
    assert campaign.name == "My Campaign"
    assert campaign.expansions == ["rough_nights", "up_in_arms"]
    DBSession.delete(campaign)


@pytest.mark.models
def test_modified(testapp):
    new_campaign = Campaign()
    new_campaign.name = "My new Campaign"
    with freeze_time("2024-01-02 03:04:05"):
        DBSession.add(new_campaign)
        new_campaign = (
            DBSession.query(Campaign).filter_by(name="My new Campaign").first()
        )
    assert new_campaign.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_campaign.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_campaign.name = "My modified Campaign"
        new_campaign = (
            DBSession.query(Campaign).filter_by(name="My modified Campaign").first()
        )
    assert new_campaign.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)


@pytest.mark.models
def test_character_relationship(new_character):
    campaign = Campaign()
    campaign.name = "Character Campaign"
    DBSession.add(campaign)
    campaign = DBSession.query(Campaign).filter_by(name="Character Campaign").first()
    new_character.campaign_id = campaign.id
    assert new_character.campaign == campaign
    assert len(campaign.characters) == 1
    assert campaign.characters[0] == new_character


@pytest.mark.models
def test_gamemaster_relationship():
    campaign = Campaign()
    campaign.name = "Gamemaster Campaign"
    DBSession.add(campaign)
    campaign = DBSession.query(Campaign).filter_by(name="Gamemaster Campaign").first()
    user_one = User(name="First Gamemaster")
    DBSession.add(user_one)
    user_two = User(name="Second Gamemaster")
    DBSession.add(user_two)
    campaign.gamemasters.append(user_one)
    campaign.gamemasters.append(user_two)
    assert len(campaign.gamemasters) == 2
    assert campaign.gamemasters[0] == user_one
    assert campaign.gamemasters[1] == user_two


@pytest.mark.models
def test_player_relationship():
    campaign = Campaign()
    campaign.name = "Player Campaign"
    DBSession.add(campaign)
    campaign = DBSession.query(Campaign).filter_by(name="Player Campaign").first()
    user_one = User(name="First Player")
    DBSession.add(user_one)
    user_two = User(name="Second Player")
    DBSession.add(user_two)
    campaign.players.append(user_one)
    campaign.players.append(user_two)
    assert len(campaign.players) == 2
    assert campaign.players[0] == user_one
    assert campaign.players[1] == user_two
