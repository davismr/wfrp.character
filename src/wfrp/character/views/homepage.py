from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(route_name="homepage")
class HomePageViews:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET", renderer=__name__ + ":../templates/homepage.pt")
    def homepage_get_view(self):
        return {}
