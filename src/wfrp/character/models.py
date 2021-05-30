import uuid

from pyramid.authorization import Allow
from pyramid.authorization import Everyone

# from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


class Character(Base):
    __tablename__ = "character"
    uid = Column(Integer, primary_key=True)
    # TODO store uuid as bytes
    uuid = Column(Text, default=str(uuid.uuid4()))
    name = Column(Text)
    species = Column(Text)
    career = Column(Text)
    experience = Column(Integer, default=0)
    weapon_skill = Column(Integer)
    ballistic_skill = Column(Integer)
    strength = Column(Integer)
    toughness = Column(Integer)
    initiative = Column(Integer)
    agility = Column(Integer)
    dexterity = Column(Integer)
    intelligence = Column(Integer)
    willpower = Column(Integer)
    fellowship = Column(Integer)


class Root(object):
    __acl__ = [(Allow, Everyone, "view"), (Allow, "group:editors", "edit")]

    def __init__(self, request):
        pass
