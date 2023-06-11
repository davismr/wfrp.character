from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget
from pyramid.security import remember
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.security import USERS
from wfrp.character.security import check_password


@view_defaults(renderer="wfrp.character:templates/homepage.pt")
class AuthViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name="login", renderer="wfrp.character:templates/login.pt")
    def login(self):
        request = self.request
        login_url = request.route_url("login")
        referrer = request.url
        if referrer == login_url:
            referrer = "/"  # never use login form itself as came_from
        came_from = request.params.get("came_from", referrer)
        message = ""
        login = ""
        password = ""
        if "form.submitted" in request.params:
            login = request.params["login"]
            password = request.params["password"]
            hashed_pw = USERS.get(login)
            if hashed_pw and check_password(password, hashed_pw):
                headers = remember(request, login)
                return HTTPFound(location=came_from, headers=headers)
            message = "Failed login"

        return dict(
            name="Login",
            message=message,
            url=request.application_url + "/login",
            came_from=came_from,
            login=login,
            password=password,
        )

    @view_config(route_name="logout")
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url("homepage")
        return HTTPFound(location=url, headers=headers)
