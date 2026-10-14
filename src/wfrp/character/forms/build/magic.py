from flask import redirect
from flask import render_template
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

from wfrp.character.forms.build.base import BaseBuildFormView


class MagicForm(FlaskForm):
    submit = SubmitField("Select Magic")


class MagicFormView(BaseBuildFormView):

    def get_form(self):
        form = MagicForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template("build/magic.jinja2", form=form)

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.character.status = "Trappings"
            next_url = url_for("build_trappings", id=self.character.id)
            return redirect(next_url)
        return render_template("build/magic.jinja2", form=form)
