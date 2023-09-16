import uuid

import pytest
from factories import CharacterFactory
from pyramid import testing
from pytest_factoryboy import register
from sqlalchemy import engine_from_config
from webtest import TestApp

from wfrp.character.models import Base
from wfrp.character.models import Character
from wfrp.character.models import DBSession

register(CharacterFactory)


@pytest.fixture(scope="session")
def testapp():
    engine = engine_from_config({"sqlalchemy.url": "sqlite:///:memory:"}, "sqlalchemy.")
    config = testing.setUp()
    config.include("pyramid_chameleon")
    config.include("wfrp.character.routes")
    config.add_static_view("static", "wfrp.character:static")
    config.add_static_view("static_deform", "deform:static")
    config.scan()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return TestApp(config.make_wsgi_app())


@pytest.fixture
def new_character(testapp):
    new_uuid = str(uuid.uuid4())
    new_character = Character(uuid=new_uuid, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.uuid == new_uuid).one()
    return character


@pytest.fixture
def second_character(testapp):
    new_uuid = str(uuid.uuid4())
    new_character = Character(uuid=new_uuid, status={"species": ""})
    DBSession.add(new_character)
    character = DBSession.query(Character).filter(Character.uuid == new_uuid).one()
    return character


@pytest.fixture
def complete_character(testapp, character_factory):
    new_character = character_factory()
    DBSession.add(new_character)
    character = (
        DBSession.query(Character).filter(Character.uuid == new_character.uuid).one()
    )
    return character
