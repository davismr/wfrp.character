from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="name")
class NameViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/name.pt")
    def get_view(self):
        return {}

    @view_config(request_method="POST", renderer=__name__ + ":../templates/name.pt")
    def submit_view(self):
        url = self.request.route_url("character", uuid=self.character.uuid)
        self.character.status = {"character": ""}
        return HTTPFound(location=url)
