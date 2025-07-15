import uuid

import pytest
from factories import CampaignFactory
from factories import CharacterFactory
from pyramid import testing
from pyramid.paster import get_appsettings
from pyramid.session import SignedCookieSessionFactory
from pytest_factoryboy import register
from sqlalchemy import engine_from_config
from webtest import TestApp

from wfrp.character.application import Base
from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.character import Character
from wfrp.character.security import SecurityPolicy

register(CampaignFactory)
register(CharacterFactory)


@pytest.fixture(scope="session")
def testapp():
    settings = get_appsettings("development.ini", name="main")
    settings["sqlalchemy.url"] = "sqlite:///:memory:"
    engine = engine_from_config(settings, "sqlalchemy.")
    config = testing.setUp(settings=settings)
    config.add_request_method(dbsession, reify=True)
    config.include("pyramid_chameleon")
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return TestApp(config.make_wsgi_app())


@pytest.fixture(scope="session")
def testapp_auth():
    settings = get_appsettings("development.ini", name="main")
    settings["sqlalchemy.url"] = "sqlite:///:memory:"
    settings["enable_auth"] = True
    engine = engine_from_config(settings, "sqlalchemy.")
    config = testing.setUp(settings=settings)
    config.add_request_method(dbsession, reify=True)
    config.include("pyramid_chameleon")
    config.include("wfrp.character.routes")
    config.include("pyramid_googleauth")
    config.set_session_factory(SignedCookieSessionFactory("secret"))
    config.set_security_policy(SecurityPolicy())
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return TestApp(config.make_wsgi_app())


@pytest.fixture
def new_character(testapp):
    new_id = uuid.uuid4()
    new_character = Character(id=new_id, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.id == new_id).one()
    return character


@pytest.fixture
def second_character(testapp):
    new_id = uuid.uuid4()
    new_character = Character(id=new_id, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.id == new_id).one()
    return character


@pytest.fixture
def complete_character(testapp, character_factory):
    new_character = character_factory()
    DBSession.add(new_character)
    character = (
        DBSession.query(Character).filter(Character.id == new_character.id).one()
    )
    return character
