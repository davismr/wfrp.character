from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms.csrf.core import CSRFTokenField
from wtforms.fields.simple import SubmitField

from wfrp.character.database import db
from wfrp.character.models.character import Character


class BaseBuildForm(FlaskForm):
    def get_fields(self):
        return [
            field
            for field in self._fields.values()
            if not isinstance(field, (CSRFTokenField, SubmitField))
        ]


class BaseBuildFormView(MethodView):

    def get_character(self, id):
        self.character = db.session.query(Character).filter(Character.id == id).one()
