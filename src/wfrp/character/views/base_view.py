from pyramid.httpexceptions import HTTPFound

from wfrp.character.models import Character
from wfrp.character.models import DBSession


class BaseView:
    def __init__(self, request):
        self.request = request
        uuid = request.matchdict["uuid"]
        self.character = DBSession.query(Character).filter(Character.uuid == uuid).one()
        if self.request.matched_route.name not in self.character.status:
            self.redirect_request(list(self.character.status)[0])

    def redirect_request(self, route):
        url = self.request.route_url(route, uuid=self.character.uuid)
        raise HTTPFound(location=url)

    def get_widget_resources(self, form):
        static_assets = form.get_widget_resources()
        static_assets["css"].append("deform:static/css/form.css")
        return static_assets
