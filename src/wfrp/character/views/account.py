from pyramid.view import view_config
from pyramid.view import view_defaults


@view_defaults(route_name="account")
class AccountPageViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(request_method="GET", renderer="wfrp.character:templates/account.pt")
    def get_view(self):
        request = self.request
        message = ""
        if "form.submitted" in request.POST:
            pass
        return dict(
            message=message,
        )
