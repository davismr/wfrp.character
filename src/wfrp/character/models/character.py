import uuid

from sqlalchemy import JSON
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.schema import ForeignKey

from wfrp.character.application import Base
from wfrp.character.data.armour import ARMOUR_DATA
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.data.trappings import TRAPPINGS_DATA
from wfrp.character.data.weapons import WEAPONS_DATA


class Character(Base):
    __tablename__ = "character"
    uid = Column(Integer, primary_key=True)
    # TODO store uuid as bytes
    uuid = Column(Text, default=str(uuid.uuid4()))
    user = Column(Integer, ForeignKey("user.uid"))
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
    fortune = Column(Integer, default=0)
    resilience = Column(Integer, default=0)
    resolve = Column(Integer, default=0)
    motivation = Column(Text)
    extra_points = Column(Integer, default=0)
    movement = Column(Integer, default=3)
    skills = Column(MutableDict.as_mutable(JSON), default={})
    talents = Column(MutableDict.as_mutable(JSON), default={})
    weapons = Column(MutableList.as_mutable(JSON), default=[])
    armour = Column(MutableList.as_mutable(JSON), default=[])
    trappings = Column(MutableList.as_mutable(JSON), default=[])
    wealth = Column(MutableDict.as_mutable(JSON), default={})
    status = Column(JSON, default={})  # this is intentionally not mutable

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
        if "Nimble Fingered" in self.talents:
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

    def calculate_wounds(self):
        total_wounds = 2 * (self.toughness // 10) + self.willpower // 10
        if "Small" not in self.talents:
            total_wounds += self.strength // 10
        if "Hardy" in self.talents:
            total_wounds += self.toughness // 10
        return total_wounds

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

    def get_filename(self):
        return self.get_display_title().lower().replace(" ", "_")

    def get_skill_level(self, skill):
        skill_data = SKILL_DATA[skill.split(" (")[0]]
        return self.skills[skill] + getattr(self, skill_data["characteristic"][0])

    def get_talent_description(self, talent):
        if talent not in TALENT_DATA:
            talent = talent.split(" (")[0]
        if "short_description" in TALENT_DATA[talent]:
            return TALENT_DATA[talent]["short_description"]
        return TALENT_DATA[talent]["description"]

    def get_encumberance_trapping(self, trapping):
        if trapping in TRAPPINGS_DATA:
            return TRAPPINGS_DATA[trapping]["Enc"]
        return None

    def total_encumberance_trappings(self):
        total = 0
        for trapping in self.trappings:
            if trapping in TRAPPINGS_DATA:
                total += TRAPPINGS_DATA[trapping]["Enc"]
        return total

    def total_encumberance_weapons(self):
        total = 0
        for weapon in self.weapons:
            if weapon in WEAPONS_DATA:
                total += WEAPONS_DATA[weapon]["Enc"]
        return total

    def total_encumberance_armour(self):
        total = 0
        for armour in self.armour:
            if armour in ARMOUR_DATA:
                total += ARMOUR_DATA[armour]["Enc"]
        return total

    def cost_characteristic(self, advance):  # noqa: C901
        """Return the experience cost of an increase in a charateristic."""
        if advance <= 5:
            return 25
        if advance <= 10:
            return 30
        if advance <= 15:
            return 40
        if advance <= 20:
            return 50
        if advance <= 25:
            return 70
        if advance <= 30:
            return 90
        if advance <= 35:
            return 120
        if advance <= 40:
            return 150
        if advance <= 45:
            return 190
        if advance <= 50:
            return 230
        if advance <= 55:
            return 280
        if advance <= 60:
            return 330
        if advance <= 65:
            return 390
        if advance <= 70:
            return 450
        return 520

    def cost_skill(self, advance):  # noqa: C901
        """Return the experience cost of an increase in a skill."""
        if advance <= 5:
            return 10
        if advance <= 10:
            return 15
        if advance <= 15:
            return 20
        if advance <= 20:
            return 30
        if advance <= 25:
            return 40
        if advance <= 30:
            return 60
        if advance <= 35:
            return 80
        if advance <= 40:
            return 110
        if advance <= 45:
            return 140
        if advance <= 50:
            return 180
        if advance <= 55:
            return 220
        if advance <= 60:
            return 270
        if advance <= 65:
            return 320
        if advance <= 70:
            return 380
        return 440

    def cost_talent(self, advance):
        """Return the experience cost of an increase in a talent."""
        return 100 * advance
