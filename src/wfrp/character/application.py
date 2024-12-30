from typing import List
from typing import NamedTuple

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.security import Allowed
from pyramid.security import Denied
from pyramid.session import SignedCookieSessionFactory
from pyramid.view import view_config
from pyramid_googleauth import GoogleSecurityPolicy
from sqlalchemy import engine_from_config

from wfrp.character.models import Base
from wfrp.character.models import DBSession

# from wfrp.character.security import SecurityPolicy


class TestGoogleSecurityPolicy(GoogleSecurityPolicy):
    class Identity(NamedTuple):
        permissions: List[str]

    def identity(self, request):
        userid = self.authenticated_userid(request)
        if userid:
            return self.Identity(permissions=["google"])
        return self.Identity([])

    def permits(self, request, _context, permission):
        if permission in self.identity(request).permissions:
            return Allowed("allowed")
        return Denied("denied")


@view_config(route_name="protected", request_method="GET", permission="google")
def protected(request):
    return Response(
        "<p>You have to be logged in to see this page.</p>"
        f"<p>Your authenticated_userid is: <code>{request.authenticated_userid}"
        "</code>.</p>"
        f"<p>Your permissions are: <code>{request.identity.permissions}</code>.</p>"
        f'<p><a href="{ request.route_url("pyramid_googleauth.logout") }">'
        "Log out</a></p>"
    )

@view_config(route_name="index", request_method="GET")
def index(request):
    return Response(
        f"<p>Your authenticated_userid is: <code>{request.authenticated_userid}</code>.</p>"
        f"<p>Your permissions are: <code>{request.identity.permissions}</code>.</p>"
        "<p>You have to be logged in to see "
        f'<a href="{ request.route_url("protected") }">the protected page</a>.</p>'
        f'<p><a href="{ request.route_url("pyramid_googleauth.login") }">Log in</a></p>'
        f'<p><a href="{ request.route_url("pyramid_googleauth.logout") }">Log out</a></p>'
    )


def configure_app(global_config, **settings):
    """Configure the pyramid api."""
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    settings["pyramid_googleauth.google_client_id"] = (
        "818352804815-dgeu215p713i1rllt3ee1vdn4v9k6hq2.apps.googleusercontent.com"
    )
    settings["pyramid_googleauth.google_client_secret"] = (
        "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"
    )
    settings["pyramid_googleauth.secret"] = "secret"
    settings["pyramid_googleauth.login_success_redirect_url"] = "/protected"
    config = Configurator(settings=settings)
    config.set_session_factory(SignedCookieSessionFactory("secret"))
    config.set_security_policy(TestGoogleSecurityPolicy())
    # config.set_security_policy(
    #     SecurityPolicy(
    #         secret=settings["wfrp.character.secret"],
    #     ),
    # )
    config.include("wfrp.character.routes")
    config.include("pyramid_googleauth")
    config.add_route("protected", "/protected")
    config.add_route("index", "/index")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    return config


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = configure_app(global_config, **settings)
    return config.make_wsgi_app()
