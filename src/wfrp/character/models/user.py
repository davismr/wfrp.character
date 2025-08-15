from datetime import datetime
from datetime import timezone
import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Uuid
from sqlalchemy import event
from sqlalchemy.orm import relationship

from wfrp.character.application import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    characters = relationship("Character", back_populates="user")
    gamemaster_campaigns = relationship(
        "Campaign", secondary="campaign_gamemaster", back_populates="gamemasters"
    )
    player_campaigns = relationship(
        "Campaign", secondary="campaign_player", back_populates="players"
    )
    name = Column(Text)
    given_name = Column(Text)
    family_name = Column(Text)
    email = Column(Text)

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)


@event.listens_for(User, "before_update")
def user_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)
