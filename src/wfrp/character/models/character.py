from datetime import datetime
from datetime import timezone
import uuid

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import Text
from sqlalchemy import Uuid
from sqlalchemy import event
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from wfrp.character.database import db


class Character(db.Model):
    __tablename__ = "character"
    id = Column(Uuid, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user_id = Column(Uuid, ForeignKey("user.id"))
    user = relationship("User", back_populates="characters")
    campaign_id = Column(Uuid, ForeignKey("campaign.id"))
    campaign = relationship("Campaign", back_populates="characters")
    expansions = Column(MutableList.as_mutable(JSON), default=[])
    name = Column(Text, default="")
    species = Column(Text, default="")
    age = Column(Integer, default=0)
    height = Column(Integer, default=0)
    hair = Column(Text, default="")
    eyes = Column(Text, default="")
    career = Column(Text, default="")
    career_class = Column(Text, default="")
    career_title = Column(Text, default="")
    career_tier = Column(Text, default="")
    career_standing = Column(Integer, default=0)
    career_path = Column(MutableList.as_mutable(JSON), default=[])
    experience = Column(Integer, default=0)
    experience_spent = Column(Integer, default=0)
    experience_cost = relationship(
        "ExperienceCost", back_populates="character", cascade="all, delete-orphan"
    )
    experience_gain = relationship(
        "ExperienceGain", back_populates="character", cascade="all, delete-orphan"
    )
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
    wounds_current = Column(Text, default="")
    psychology = Column(Text, default="")
    corruption = Column(Text, default="")
    fate = Column(Integer, default=0)
    fortune = Column(Integer, default=0)
    resilience = Column(Integer, default=0)
    resolve = Column(Integer, default=0)
    motivation = Column(Text, default="")
    short_term_ambition = Column(Text, default="")
    long_term_ambition = Column(Text, default="")
    extra_points = Column(Integer, default=0)
    movement = Column(Integer, default=3)
    skills = Column(MutableDict.as_mutable(JSON), default={})
    talents = Column(MutableDict.as_mutable(JSON), default={})
    chanties = Column(MutableList.as_mutable(JSON), default=[])
    petty_magic = Column(MutableList.as_mutable(JSON), default=[])
    arcane_magic = Column(MutableList.as_mutable(JSON), default=[])
    lore_magic = Column(MutableList.as_mutable(JSON), default=[])
    religion = Column(Text, default="")
    miracles = Column(MutableList.as_mutable(JSON), default=[])
    weapons = Column(MutableList.as_mutable(JSON), default=[])
    armour = Column(MutableList.as_mutable(JSON), default=[])
    trappings = Column(MutableList.as_mutable(JSON), default=[])
    brass_pennies = Column(Integer, default=0)
    silver_shillings = Column(Integer, default=0)
    gold_crowns = Column(Integer, default=0)
    status = Column(Text, default="create")
    create_data = Column(MutableList.as_mutable(JSON), default=[])

    def __init__(self, **kwargs):
        kwargs["id"] = kwargs.get("id", uuid.uuid4())
        super().__init__(**kwargs)

    @property
    def weapon_skill(self):
        weapon_skill = self.weapon_skill_initial + self.weapon_skill_advances
        if "Warrior Born" in self.talents:
            weapon_skill += 5
        return weapon_skill

    @property
    def ballistic_skill(self):
        ballistic_skill = self.ballistic_skill_initial + self.ballistic_skill_advances
        if "Marksman" in self.talents:
            ballistic_skill += 5
        return ballistic_skill

    @property
    def strength(self):
        strength = self.strength_initial + self.strength_advances
        if "Very Strong" in self.talents:
            strength += 5
        return strength

    @property
    def toughness(self):
        toughness = self.toughness_initial + self.toughness_advances
        if "Very Resilient" in self.talents:
            toughness += 5
        return toughness

    @property
    def initiative(self):
        initiative = self.initiative_initial + self.initiative_advances
        if "Sharp" in self.talents:
            initiative += 5
        return initiative

    @property
    def agility(self):
        agility = self.agility_initial + self.agility_advances
        if "Lightning Reflexes" in self.talents:
            agility += 5
        return agility

    @property
    def dexterity(self):
        dexterity = self.dexterity_initial + self.dexterity_advances
        if "Nimble-fingered" in self.talents:
            dexterity += 5
        return dexterity

    @property
    def intelligence(self):
        intelligence = self.intelligence_initial + self.intelligence_advances
        if "Savvy" in self.talents:
            intelligence += 5
        return intelligence

    @property
    def willpower(self):
        willpower = self.willpower_initial + self.willpower_advances
        if "Coolheaded" in self.talents:
            willpower += 5
        return willpower

    @property
    def fellowship(self):
        fellowship = self.fellowship_initial + self.fellowship_advances
        if "Suave" in self.talents:
            fellowship += 5
        return fellowship

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


@event.listens_for(Character, "before_update")
def character_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)
