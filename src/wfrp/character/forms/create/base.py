from flask import request
from flask import url_for
from flask.views import MethodView
from flask_wtf import FlaskForm
from werkzeug.routing.exceptions import RequestRedirect
from wtforms import SelectMultipleField
from wtforms.csrf.core import CSRFTokenField
from wtforms.fields.simple import SubmitField
from wtforms.widgets import CheckboxInput
from wtforms.widgets import ListWidget

from wfrp.character.database import db
from wfrp.character.models.character import Character


class BaseCreateForm(FlaskForm):

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


class BaseCreateFormView(MethodView):

    def get_character(self, id):
        self.character = db.session.query(Character).filter(Character.id == id).one()
        self.check_status()

    def check_status(self):
        if self.character.status in ["Active", "create"]:
            return
        endpoint = request.url_rule.endpoint
        expected_endpoint = f"create_{self.character.status.lower()}"
        if endpoint != expected_endpoint:
            redirect_url = url_for(expected_endpoint, id=self.character.id)
            raise RequestRedirect(redirect_url)


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
