import uuid

import pytest
from pyramid import testing
from sqlalchemy import engine_from_config

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
