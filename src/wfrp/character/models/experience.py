from datetime import datetime
from datetime import timezone
import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from wfrp.character.application import Base


class ExperienceCost(Base):
    __tablename__ = "experience_cost"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    character_id = Column(Uuid, ForeignKey("character.id"))
    character = relationship("Character", back_populates="experience_cost")
    type = Column(String)
    name = Column(String)
    cost = Column(Integer)

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)


class ExperienceGain(Base):
    __tablename__ = "experience_gain"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    character_id = Column(Uuid, ForeignKey("character.id"))
    character = relationship("Character", back_populates="experience_gain")
    amount = Column(Integer)
    reason = Column(String)

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)
