from pyramid.view import view_config

from wfrp.character.skill_data import SKILL_DATA
from wfrp.character.talent_data import TALENT_DATA
from wfrp.character.views.base_view import BaseView


class CharacterViews(BaseView):
    @view_config(
        route_name="character_full", renderer="wfrp.character:templates/character.pt"
    )
    def full_view(self):
        return {
            "character": self.character,
            "skill_data": SKILL_DATA,
            "talent_data": TALENT_DATA,
        }

    @view_config(
        route_name="character_summary", renderer="wfrp.character:templates/summary.pt"
    )
    def summary_view(self):
        return {"character": self.character}
