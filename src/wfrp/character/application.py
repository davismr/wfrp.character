from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from wfrp.character.models import Base
from wfrp.character.models import DBSession


def configure_app(global_config, **settings):
    """Configure the pyramid api."""
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy("secret")
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    return config


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = configure_app(global_config, **settings)
    return config.make_wsgi_app()
