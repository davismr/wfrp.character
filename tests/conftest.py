import pytest

from wfrp.character.app import create_app
from wfrp.character.database import init_db
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
