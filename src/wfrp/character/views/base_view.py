import uuid

from wfrp.character.models.character import Character


class BaseView:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        id = request.matchdict["id"]
        self.character = (
            request.dbsession.query(Character)
            .filter(Character.id == uuid.UUID(id))
            .one()
        )

    def get_widget_resources(self, form):
        static_assets = form.get_widget_resources()
        static_assets["css"].append("deform:static/css/form.css")
        return static_assets
