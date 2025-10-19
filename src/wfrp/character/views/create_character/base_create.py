import uuid

from pyramid.httpexceptions import HTTPFound

from wfrp.character.models.character import Character


class BaseCreateView:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        id = request.matchdict["id"]
        self.character = (
            request.dbsession.query(Character)
            .filter(Character.id == uuid.UUID(id))
            .one()
        )
        if (
            self.character.status == "create"
            and self.request.matched_route.name not in self.character.create_data
        ):
            self.redirect_request(list(self.character.create_data)[0])

    def redirect_request(self, route):
        url = self.request.route_url(route, id=self.character.id)
        raise HTTPFound(location=url)

    def get_widget_resources(self, form):
        static_assets = form.get_widget_resources()
        static_assets["css"].append("deform:static/css/form.css")
        return static_assets
