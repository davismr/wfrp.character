from datetime import datetime
from datetime import timezone

from freezegun import freeze_time

from wfrp.character.database import db
from wfrp.character.models.campaign import Campaign
from wfrp.character.models.user import User


def test_add_campaign(client):
    # make sure db is empty
    db.session.query(Campaign).delete()
    new_campaign = Campaign()
    new_campaign.name = "My Campaign"
    new_campaign.expansions = ["rough_nights", "up_in_arms"]
    db.session.add(new_campaign)
    assert db.session.query(Campaign).count() == 1
    campaign = db.session.query(Campaign).first()
    assert campaign.name == "My Campaign"
    assert campaign.expansions == ["rough_nights", "up_in_arms"]
    db.session.delete(campaign)


def test_modified(client):
    new_campaign = Campaign()
    new_campaign.name = "My new Campaign"
    with freeze_time("2024-01-02 03:04:05"):
        db.session.add(new_campaign)
        new_campaign = (
            db.session.query(Campaign).filter_by(name="My new Campaign").first()
        )
    assert new_campaign.created == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    assert new_campaign.modified == datetime(2024, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
    with freeze_time("2025-06-07 08:09:10"):
        new_campaign.name = "My modified Campaign"
        new_campaign = (
            db.session.query(Campaign).filter_by(name="My modified Campaign").first()
        )
    assert new_campaign.modified == datetime(2025, 6, 7, 8, 9, 10, tzinfo=timezone.utc)


def test_character_relationship(new_character):
    campaign = Campaign()
    campaign.name = "Character Campaign"
    db.session.add(campaign)
    campaign = db.session.query(Campaign).filter_by(name="Character Campaign").first()
    new_character.campaign_id = campaign.id
    assert new_character.campaign == campaign
    assert len(campaign.characters) == 1
    assert campaign.characters[0] == new_character


def test_gamemaster_relationship(client):
    campaign = Campaign()
    campaign.name = "Gamemaster Campaign"
    db.session.add(campaign)
    campaign = db.session.query(Campaign).filter_by(name="Gamemaster Campaign").first()
    user_one = User(name="First Gamemaster")
    db.session.add(user_one)
    user_two = User(name="Second Gamemaster")
    db.session.add(user_two)
    campaign.gamemasters.append(user_one)
    campaign.gamemasters.append(user_two)
    assert len(campaign.gamemasters) == 2
    assert campaign.gamemasters[0] == user_one
    assert campaign.gamemasters[1] == user_two


def test_player_relationship(client):
    campaign = Campaign()
    campaign.name = "Player Campaign"
    db.session.add(campaign)
    campaign = db.session.query(Campaign).filter_by(name="Player Campaign").first()
    user_one = User(name="First Player")
    db.session.add(user_one)
    user_two = User(name="Second Player")
    db.session.add(user_two)
    campaign.players.append(user_one)
    campaign.players.append(user_two)
    assert len(campaign.players) == 2
    assert campaign.players[0] == user_one
    assert campaign.players[1] == user_two
