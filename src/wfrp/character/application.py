import os

from dotenv import load_dotenv
from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.session import SignedCookieSessionFactory
from pyramid.settings import asbool
from sqlalchemy import engine_from_config
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register

from wfrp.character import __version__

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()
load_dotenv()


def configure_app(global_config, **settings):
    """Configure the pyramid api."""
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    if "wfrp.character.enable_auth" not in settings:
        settings["wfrp.character.enable_auth"] = False
    enable_auth = asbool(settings.get("wfrp.character.enable_auth"))
    settings["enable_auth"] = enable_auth
    settings["google-site-verification"] = os.environ.get("google-site-verification")
    settings["pyramid_googleauth.google_client_id"] = os.environ.get("google_client_id")
    settings["pyramid_googleauth.google_client_secret"] = os.environ.get(
        "google_client_secret"
    )
    settings["pyramid_googleauth.secret"] = "secret"
    settings["pyramid_googleauth.login_success_redirect_url"] = "/google"
    config = Configurator(settings=settings)
    config.set_session_factory(SignedCookieSessionFactory("secret"))
    if enable_auth is True:
        # to prevent circular imports
        from wfrp.character.security import SecurityPolicy

        config.set_security_policy(SecurityPolicy())
    config.include("pyramid_googleauth")
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.add_request_method(dbsession, reify=True)
    config.scan()
    return config


def dbsession(request):
    return DBSession


@subscriber(NewRequest)
def add_package_version(event):
    event.request.package_version = __version__


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = configure_app(global_config, **settings)
    return config.make_wsgi_app()
