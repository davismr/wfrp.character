from flask import redirect
from flask import render_template
from flask import url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

from wfrp.character.database import db
from wfrp.character.forms.build.base import BaseBuildForm
from wfrp.character.models.character import Character


class NewForm(FlaskForm):
    submit = SubmitField("Build Character")


class NewFormView(BaseBuildForm):

    def create_character(self):
        self.character = Character()
        db.session.add(self.character)
        db.session.commit()

    def get_form(self):
        form = NewForm()
        return form

    def get(self):
        form = self.get_form()
        return render_template("build/new.jinja2", title="New", form=form)

    def post(self):
        form = self.get_form()
        if form.validate_on_submit():
            self.create_character()
            self.character.status = "species"
            next_url = url_for("build_species", id=self.character.id)
            return redirect(next_url)
        return render_template("build/new.jinja2", title="New", form=form)
