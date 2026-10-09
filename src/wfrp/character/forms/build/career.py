from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

from flask import redirect
from flask import render_template
from flask import url_for

from wfrp.character.database import db
from wfrp.character.forms.build.base import BaseBuildForm
from wfrp.data.tables.careers import get_career, get_career_list
from wfrp.data.dice import roll_d100


class CareerForm(FlaskForm):
    career = RadioField("Career", validators=[DataRequired()])
    submit = SubmitField("Select Career")


class CareerFormView(BaseBuildForm):

    def initialise_form(self):
        if not self.character.create_data:
            die_roll = roll_d100()
            self.character.create_data = [
                (die_roll, get_career(self.character.species, die_roll))
            ]
            db.session.commit()

    def get_form(self):
        self.initialise_form()
        form = CareerForm(career=self.character.create_data[0][1])
        form.career.choices = list(get_career_list(self.character.species).values())
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "build/career.jinja2", title="Career", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            next_url = url_for("build_career", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "build/career.jinja2", title="Career", form=form, character=self.character
        )
