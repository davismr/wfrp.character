import uuid

from pyramid.authorization import Allow
from pyramid.authorization import Everyone

# from pyramid_sqlalchemy import BaseObject
from sqlalchemy import JSON
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
    experience_spent = Column(Integer, default=0)
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
    wounds = Column(Integer)
    fate = Column(Integer, default=0)
    resilience = Column(Integer, default=0)
    extra_points = Column(Integer)
    movement = Column(Integer, default=3)
    status = Column(JSON, default={})

    def calculate_wounds(self):
        if self.species == "Halfling":
            return 2 * (self.toughness // 10) + self.willpower // 10
        return self.strength // 10 + 2 * (self.toughness // 10) + self.willpower // 10

    def get_display_title(self):
        display_title = ""
        if self.name:
            display_title += self.name
            display_title += " the "
        if self.species:
            display_title += self.species
        if self.career:
            display_title += " "
            display_title += self.career
        if not display_title:
            display_title += "Unknown"
        return display_title


class Root(object):
    __acl__ = [(Allow, Everyone, "view"), (Allow, "group:editors", "edit")]

    def __init__(self, request):
        pass
