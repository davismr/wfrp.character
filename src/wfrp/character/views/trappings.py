from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="trappings")
class TrappingsViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/trappings.pt")
    def get_view(self):
        return {}

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/trappings.pt"
    )
    def submit_view(self):
        url = self.request.route_url("details", uuid=self.character.uuid)
        self.character.status = {"details": ""}
        return HTTPFound(location=url)
