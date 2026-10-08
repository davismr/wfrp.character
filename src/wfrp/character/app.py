import os

from flask import Flask

from wfrp.character.database import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is not None:
        app.config.from_object(test_config)
    else:
        app.config.from_mapping(
            SECRET_KEY="dev",
            DATABASE=os.path.join(os.getcwd(), "wfrp.sqlite"),
        )
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/wfrp.sqlite"
    db.init_app(app)
    return app
