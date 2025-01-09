from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


def configure_app(global_config, **settings):
    """Configure the pyramid api."""
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    if "wfrp.character.enable_auth" not in settings:
        settings["wfrp.character.enable_auth"] = False
    enable_auth = settings.get("wfrp.character.enable_auth")
    config = Configurator(settings=settings)
    # to prevent circular imports
    if enable_auth is True:
        from wfrp.character.security import SecurityPolicy

        config.set_security_policy(
            SecurityPolicy(
                secret=settings["wfrp.character.secret"],
            ),
        )
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.add_request_method(dbsession, reify=True)
    config.scan()
    return config


def dbsession(request):
    return DBSession


def main(global_config, **settings):
    """Return a Pyramid WSGI application."""
    config = configure_app(global_config, **settings)
    return config.make_wsgi_app()
