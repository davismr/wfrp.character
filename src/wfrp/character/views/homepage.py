from pyramid.renderers import render
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(route_name="homepage")
class HomePageViews:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def homepage_get_view(self):
        result = render(
            __name__ + ":../templates/homepage.pt", {}, request=self.request
        )
        return Response(result)
