from flask import redirect
from flask import render_template
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

from wfrp.character.forms.build.base import BaseBuildFormView


class NameForm(FlaskForm):
    submit = SubmitField("Select Name")


class NameFormView(BaseBuildFormView):

    def get_form(self):
        form = NameForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template("build/name.jinja2", form=form)

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.character.status = "Active"
            next_url = url_for("character_view", id=self.character.id)
            return redirect(next_url)
        return render_template("build/name.jinja2", form=form)
