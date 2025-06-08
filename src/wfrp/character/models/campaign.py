from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from wfrp.character.application import Base


class Campaign(Base):
    __tablename__ = "campaign"
    uid = Column(Integer, primary_key=True)
    name = Column(Text)
