from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

from wfrp.character.application import Base


class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    name = Column(Text)
    given_name = Column(Text)
    family_name = Column(Text)
    email = Column(Text)
