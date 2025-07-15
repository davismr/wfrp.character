from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import NoResultFound

from wfrp.character.models.user import User


@view_defaults(renderer="wfrp.character:templates/homepage.pt")
class AuthViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name="google_login")
    def google_login(self):
        user_email = self.request.authenticated_userid
        try:
            self.request.dbsession.query(User).filter(User.email == user_email).one()
        except NoResultFound:
            url = self.request.route_url("register")
            raise HTTPFound(location=url)
        url = self.request.route_url("homepage")
        raise HTTPFound(location=url)

    @view_config(route_name="logout")
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url("homepage")
        return HTTPFound(location=url, headers=headers)

    @view_config(route_name="register", renderer="wfrp.character:templates/register.pt")
    def register(self):
        request = self.request
        message = ""
        if request.session.get("user"):
            email = request.session.get("user")["email"]
            name = request.session.get("user")["name"]
            given_name = request.session.get("user")["given_name"]
            family_name = request.session.get("user")["family_name"]
        else:
            email = ""
            name = ""
            given_name = ""
            family_name = ""
        if "form.submitted" in request.POST:
            new_user = User(
                email=email, name=name, given_name=given_name, family_name=family_name
            )
            request.dbsession.add(new_user)
            return HTTPFound(location=self.request.route_url("homepage"))
        return dict(
            message=message,
            name=name,
            given_name=given_name,
            family_name=family_name,
            email=email,
        )
