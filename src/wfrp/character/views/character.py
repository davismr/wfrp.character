import logging

from pyramid.renderers import render_to_response
from pyramid.response import Response
from pyramid.view import view_config

from wfrp.character.data.armour import ARMOUR_DATA
from wfrp.character.data.skills import SKILL_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.data.weapons import WEAPONS_DATA
from wfrp.character.views.create_character.base_view import BaseView

logger = logging.getLogger(__name__)

try:
    from weasyprint import HTML

    WEASYPRINT_INSTALLED = True
except (ImportError, OSError):
    logger.info("weasyprint not correctly installed")
    WEASYPRINT_INSTALLED = False


class CharacterViews(BaseView):
    @view_config(
        route_name="character_full", renderer="wfrp.character:templates/character.pt"
    )
    def full_view(self):
        return {
            "character": self.character,
            "skill_data": SKILL_DATA,
            "talent_data": TALENT_DATA,
            "weapons_data": WEAPONS_DATA,
            "armour_data": ARMOUR_DATA,
        }

    @view_config(
        route_name="character_summary", renderer="wfrp.character:templates/summary.pt"
    )
    def summary_view(self):
        return {"character": self.character}

    @view_config(route_name="pdf_print")
    def pdf_print(self):
        html = render_to_response(
            "wfrp.character:templates/pdf.pt", self.full_view(), request=self.request
        )
        filename = f"{self.character.get_filename()}.pdf"
        response = Response(body=HTML(string=html.body).write_pdf())
        response.headers["Content-Disposition"] = f"attachment;filename={filename}"
        return response
