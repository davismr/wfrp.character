from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models import Character
from wfrp.character.models import DBSession
from wfrp.character.utils import roll_2d10

ATTRIBUTES = [
    "Weapon Skill",
    "Ballistic Skill",
    "Strength",
    "Toughness",
    "Initiative",
    "Agility",
    "Dexterity",
    "Intelligence",
    "Willpower",
    "Fellowship",
]


@view_defaults(route_name="attributes")
class AttributesViews:
    def __init__(self, request):
        self.request = request
        uuid = request.matchdict["uuid"]
        self.character = DBSession.query(Character).filter(Character.uuid == uuid).one()

    def _roll_base_attributes(self):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = roll_2d10()
        return attributes

    def _get_bonus_attributes(self, species):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = 20
        if species == "Human":
            pass
        elif species == "Halfling":
            attributes["Weapon Skill"] += -10
            attributes["Ballistic Skill"] += 10
            attributes["Strength"] += -10
            attributes["Dexterity"] += -10
            attributes["Willpower"] += -10
            attributes["Fellowship"] += -10
        elif species == "Dwarf":
            attributes["Weapon Skill"] += 10
            attributes["Toughness"] += 10
            attributes["Agility"] += -10
            attributes["Dexterity"] += 10
            attributes["Willpower"] += 20
            attributes["Fellowship"] += -10
        elif species in ["High Elf", "Wood Elf"]:
            attributes["Weapon Skill"] += 10
            attributes["Ballistic Skill"] += 10
            attributes["Initiative"] += 20
            attributes["Agility"] += 10
            attributes["Dexterity"] += 10
            attributes["Intelligence"] += 10
            attributes["Willpower"] += 10
        else:
            raise NotImplementedError(f"{species} is not defined for bonus attributes")
        return attributes

    @view_config(
        request_method="GET", renderer=__name__ + ":../templates/attributes.pt"
    )
    def new_career_view(self):
        base_attributes = self._roll_base_attributes()
        bonus_attributes = self._get_bonus_attributes(self.character.species)
        total_attributes = 0
        for attribute in base_attributes:
            total_attributes += base_attributes[attribute]
        return {
            "base_attributes": base_attributes,
            "bonus_attributes": bonus_attributes,
            "total_attributes": total_attributes,
        }

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/attributes.pt"
    )
    def submit_career_view(self):
        url = self.request.route_url("homepage")
        return HTTPFound(location=url)