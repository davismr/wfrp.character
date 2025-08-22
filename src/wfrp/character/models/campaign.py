from datetime import datetime
from datetime import timezone
import uuid

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy import Uuid
from sqlalchemy import event
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from wfrp.character.application import Base
from wfrp.character.data.expansions import EXPANSIONS


class Campaign(Base):
    __tablename__ = "campaign"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    characters = relationship("Character", back_populates="campaign")
    gamemasters = relationship(
        "User", secondary="campaign_gamemaster", back_populates="gamemaster_campaigns"
    )
    players = relationship(
        "User", secondary="campaign_player", back_populates="player_campaigns"
    )
    name = Column(Text)
    expansions = Column(MutableList.as_mutable(JSON), default=[])
    sessions = relationship("CampaignSession", back_populates="campaign")

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)

    def get_display_title(self):
        return self.name

    def get_expansion_titles(self):
        results = []
        for expansion in self.expansions:
            results.append(EXPANSIONS[expansion]["title"])
        return results


@event.listens_for(Campaign, "before_update")
def campaign_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)


class CampaignSession(Base):
    __tablename__ = "campaign_session"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    session_date = Column(Date)
    title = Column(Text)
    summary = Column(Text)
    campaign_id = Column(Uuid, ForeignKey("campaign.id"))
    campaign = relationship("Campaign", back_populates="sessions")
    experience_gain = relationship("ExperienceGain", back_populates="campaign_session")

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)


campaign_gamemaster = Table(
    "campaign_gamemaster",
    Base.metadata,
    Column("campaign_id", ForeignKey("campaign.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)


campaign_player = Table(
    "campaign_player",
    Base.metadata,
    Column("campaign_id", ForeignKey("campaign.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)
