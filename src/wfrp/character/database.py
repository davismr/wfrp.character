from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from wfrp.character.models import campaign  # noqa
    from wfrp.character.models import character  # noqa
    from wfrp.character.models import experience  # noqa
    from wfrp.character.models import user  # noqa

    with app.app_context():
        db.create_all()
