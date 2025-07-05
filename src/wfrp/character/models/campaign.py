import uuid

from sqlalchemy import JSON
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.schema import ForeignKey

from wfrp.character.application import Base


class Campaign(Base):
    __tablename__ = "campaign"
    uid = Column(Integer, primary_key=True)
    uuid = Column(Text, default=str(uuid.uuid4()))
    user = Column(Integer, ForeignKey("user.uid"))
    name = Column(Text)
    expansions = Column(MutableList.as_mutable(JSON), default=[])
