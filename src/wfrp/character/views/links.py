from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(route_name="links", renderer="wfrp.character:templates/links.pt")
class LinksViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config()
    def links_view(self):
        return {}
