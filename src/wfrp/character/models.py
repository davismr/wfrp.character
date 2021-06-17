import uuid

from pyramid.authorization import Allow
from pyramid.authorization import Everyone

# from pyramid_sqlalchemy import BaseObject
from sqlalchemy import JSON
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.mutable import MutableList
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
    age = Column(Integer)
    height = Column(Integer)
    hair = Column(Text)
    eyes = Column(Text)
    career = Column(Text)
    career_class = Column(Text)
    career_title = Column(Text)
    career_level = Column(Text)
    career_tier = Column(Text)
    career_standing = Column(Integer, default=0)
    career_path = Column(MutableList.as_mutable(JSON), default=[])
    experience = Column(Integer, default=0)
    experience_spent = Column(Integer, default=0)
    weapon_skill_initial = Column(Integer, default=0)
    ballistic_skill_initial = Column(Integer, default=0)
    strength_initial = Column(Integer, default=0)
    toughness_initial = Column(Integer, default=0)
    initiative_initial = Column(Integer, default=0)
    agility_initial = Column(Integer, default=0)
    dexterity_initial = Column(Integer, default=0)
    intelligence_initial = Column(Integer, default=0)
    willpower_initial = Column(Integer, default=0)
    fellowship_initial = Column(Integer, default=0)
    weapon_skill_advances = Column(Integer, default=0)
    ballistic_skill_advances = Column(Integer, default=0)
    strength_advances = Column(Integer, default=0)
    toughness_advances = Column(Integer, default=0)
    initiative_advances = Column(Integer, default=0)
    agility_advances = Column(Integer, default=0)
    dexterity_advances = Column(Integer, default=0)
    intelligence_advances = Column(Integer, default=0)
    willpower_advances = Column(Integer, default=0)
    fellowship_advances = Column(Integer, default=0)
    wounds = Column(Integer, default=0)
    fate = Column(Integer, default=0)
    resilience = Column(Integer, default=0)
    extra_points = Column(Integer, default=0)
    movement = Column(Integer, default=3)
    skills = Column(MutableDict.as_mutable(JSON), default={})
    talents = Column(MutableList.as_mutable(JSON), default=[])
    trappings = Column(JSON, default=[])
    wealth = Column(JSON, default={})
    status = Column(JSON, default={})

    @property
    def weapon_skill(self):
        return self.weapon_skill_initial + self.weapon_skill_advances

    @property
    def ballistic_skill(self):
        return self.ballistic_skill_initial + self.ballistic_skill_advances

    @property
    def strength(self):
        return self.strength_initial + self.strength_advances

    @property
    def toughness(self):
        return self.toughness_initial + self.toughness_advances

    @property
    def initiative(self):
        return self.initiative_initial + self.initiative_advances

    @property
    def agility(self):
        return self.agility_initial + self.agility_advances

    @property
    def dexterity(self):
        return self.dexterity_initial + self.dexterity_advances

    @property
    def intelligence(self):
        return self.intelligence_initial + self.intelligence_advances

    @property
    def willpower(self):
        return self.willpower_initial + self.willpower_advances

    @property
    def fellowship(self):
        return self.fellowship_initial + self.fellowship_advances

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
