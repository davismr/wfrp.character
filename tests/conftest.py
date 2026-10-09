import uuid

import pytest

from wfrp.character.app import create_app
from wfrp.character.database import db
from wfrp.character.database import init_db
from wfrp.character.models.character import Character
from wfrp.character.routes import register_routes


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    TESTING = True


@pytest.fixture
def client(scope="session"):
    app = create_app(test_config=Config)
    init_db(app)
    with app.app_context():
        register_routes(app)
        yield app.test_client()


@pytest.fixture
def new_character(client):
    new_id = uuid.uuid4()
    new_character = Character(id=new_id)
    db.session.add(new_character)
    character = db.session.query(Character).filter(Character.id == new_id).one()
    return character
