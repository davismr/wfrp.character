from datetime import datetime
from datetime import timezone
import uuid

from sqlalchemy import Column
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

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)

    def get_display_title(self):
        return self.name


@event.listens_for(Campaign, "before_update")
def campaign_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)


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
