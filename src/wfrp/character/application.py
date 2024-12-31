from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from wfrp.character.models.character import Base
from wfrp.character.models.character import DBSession
from wfrp.character.security import SecurityPolicy


def configure_app(global_config, **settings):
    """Configure the pyramid api."""
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.set_security_policy(
        SecurityPolicy(
            secret=settings["wfrp.character.secret"],
        ),
    )
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    return config


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = configure_app(global_config, **settings)
    return config.make_wsgi_app()
