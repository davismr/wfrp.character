from flask import redirect
from flask import render_template
from flask import url_for
from flask_wtf import FlaskForm
from wfrp.data.species import SPECIES_DATA
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.character.database import db
from wfrp.character.forms.build.base import BaseBuildFormView


class PhysicalForm(FlaskForm):
    eye_colour = RadioField("Eye Colour", validators=[DataRequired()])
    hair_colour = RadioField("Hair Colour", validators=[DataRequired()])
    submit = SubmitField("Select")


class PhysicalFormView(BaseBuildFormView):

    def initialise_form(self):
        if not self.character.create_data:
            species = self.character.species
            die_roll = SPECIES_DATA[species]["age"][1]()
            age = die_roll + SPECIES_DATA[species]["age"][0]
            self.character.age = age
            self.character.create_data = [(die_roll, age)]
            die_roll = SPECIES_DATA[species]["height"][1]()
            height = die_roll + SPECIES_DATA[species]["height"][0]
            self.character.height = height
            self.character.create_data.append((die_roll, self.character.height))
            db.session.commit()

    def get_form(self):
        self.initialise_form()
        form = PhysicalForm()
        form.eye_colour.choices = SPECIES_DATA[self.character.species]["eye_colour"]
        form.hair_colour.choices = SPECIES_DATA[self.character.species]["hair_colour"]
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "build/physical.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form.data)
            next_url = url_for("build_career", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "build/physical.jinja2", form=form, character=self.character
        )

    def update_character(self, data):
        self.character.eyes = data["eye_colour"]
        self.character.hair = data["hair_colour"]
        self.character.status = "career"
        self.character.create_data = []
        db.session.commit()
