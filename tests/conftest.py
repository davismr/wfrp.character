import uuid

import pytest
from pyramid import testing
from sqlalchemy import engine_from_config
from webtest import TestApp

from wfrp.character.models import Base
from wfrp.character.models import Character
from wfrp.character.models import DBSession


@pytest.fixture(scope="session")
def session_db():
    engine = engine_from_config({"sqlalchemy.url": "sqlite://"}, "sqlalchemy.")
    config = testing.setUp()
    config.include("pyramid_chameleon")
    config.include("wfrp.character.routes")
    config.scan()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from wfrp.character.application import main

    settings = {
        "sqlalchemy.url": "sqlite:///:memory:",
        "wfrp.character.secret": "secret",
    }
    # app = main({}, **settings)
    # app = main({}, **{"sqlalchemy.url": "sqlite://", "wfrp.character.secret": "secret"})
    # import pdb;pdb.set_trace()

    engine = engine_from_config(settings, "sqlalchemy.")
    config = testing.setUp()
    config.include("pyramid_chameleon")
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    # SessionFactory = app.registry["dbsession_factory"]
    # engine = SessionFactory().bind
    # Base.metadata.create_all(bind=engine)
    # DBSession.configure(bind=engine)
    # Base.metadata.bind = engine
    return TestApp(config.make_wsgi_app())


@pytest.fixture
def new_character(session_db):
    new_uuid = str(uuid.uuid4())
    new_character = Character(uuid=new_uuid, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.uuid == new_uuid).one()
    return character


@pytest.fixture
def second_character(session_db):
    new_uuid = str(uuid.uuid4())
    new_character = Character(uuid=new_uuid, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.uuid == new_uuid).one()
    return character
