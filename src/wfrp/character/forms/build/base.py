from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms.csrf.core import CSRFTokenField
from wtforms.fields.simple import SubmitField
from wtforms.widgets import CheckboxInput
from wtforms.widgets import ListWidget
from wtforms import SelectMultipleField

from wfrp.character.database import db
from wfrp.character.models.character import Character


class BaseBuildForm(FlaskForm):
    def get_fields(self, subform=None):
        if subform is None:
            fields = self._fields.values()
        else:
            fields = self.__getattribute__(subform)._fields.values()
        return [
            field
            for field in fields
            if not isinstance(field, (CSRFTokenField, SubmitField))
        ]


class BaseBuildFormView(MethodView):

    def get_character(self, id):
        self.character = db.session.query(Character).filter(Character.id == id).one()


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
