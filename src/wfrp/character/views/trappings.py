from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_skills import SKILL_LIST
from wfrp.character.trappings import CLASS_TRAPPINGS
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="trappings")
class TrappingsViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/trappings.pt")
    def get_view(self):
        career_data = SKILL_LIST[self.character.career]
        class_trappings = CLASS_TRAPPINGS[career_data["class"]]
        # TODO find a better way to do this
        career_details = career_data[list(career_data)[1]]
        career_trappings = career_details["trappings"]
        return {
            "class_trappings": class_trappings,
            "career_trappings": career_trappings,
        }

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/trappings.pt"
    )
    def submit_view(self):
        url = self.request.route_url("details", uuid=self.character.uuid)
        self.character.status = {"details": ""}
        return HTTPFound(location=url)
