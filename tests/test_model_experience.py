from datetime import datetime
from datetime import timezone

from freezegun import freeze_time
import pytest

from wfrp.character.application import DBSession
from wfrp.character.models.experience import ExperienceCost
from wfrp.character.models.experience import ExperienceGain


@pytest.mark.models
def test_experience_cost(new_character):
    experience_cost = ExperienceCost(
        character_id=new_character.id,
        type="characteristic",
        cost=10,
        name="Intelligence",
    )
    with freeze_time("2025-01-02 03:04:05"):
        DBSession.add(experience_cost)
        assert DBSession.query(ExperienceCost).count() == 1
        experience_cost = DBSession.query(ExperienceCost).first()
    assert experience_cost.character_id == new_character.id
    assert experience_cost.type == "characteristic"
    assert experience_cost.cost == 10
    assert experience_cost.name == "Intelligence"
    assert experience_cost.created == datetime(2025, 1, 2, 3, 4, 5, tzinfo=timezone.utc)


@pytest.mark.models
def test_experience_gain(new_character):
    experience_gain = ExperienceGain(
        character_id=new_character.id,
        amount=1000,
        reason="Free experience",
    )
    with freeze_time("2025-01-02 03:04:05"):
        DBSession.add(experience_gain)
        assert DBSession.query(ExperienceGain).count() == 1
        experience_gain = DBSession.query(ExperienceGain).first()
    assert experience_gain.character_id == new_character.id
    assert experience_gain.amount == 1000
    assert experience_gain.reason == "Free experience"
    assert experience_gain.created == datetime(2025, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
