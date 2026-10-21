from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.data.dice import roll_d100
from wfrp.data.species import SPECIES_DATA
from wfrp.data.tables.species import SPECIES
from wfrp.data.tables.species import get_species

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class SpeciesForm(BaseCreateForm):
    species = RadioField("Species", validators=[DataRequired()])
    submit = SubmitField("Select Species")


class SpeciesFormView(BaseCreateFormView):

    def initialise_form(self):
        if not self.character.create_data:
            die_roll = roll_d100()
            self.character.create_data = {
                "die_roll": die_roll,
                "species": get_species(die_roll),
            }
            db.session.commit()

    def get_form(self):
        self.initialise_form()
        form = SpeciesForm(species=self.character.create_data["species"])
        form.species.choices = list(SPECIES.values())
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/species.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form.data)
            next_url = url_for("create_physical", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/species.jinja2", form=form, character=self.character
        )

    def update_character(self, data):
        species = data["species"]
        self.character.species = species
        self.character.fate = SPECIES_DATA[species]["fate"]
        self.character.fortune = SPECIES_DATA[species]["fortune"]
        self.character.movement = SPECIES_DATA[species]["movement"]
        if species == self.character.create_data["species"]:
            self.character.fortune += 1
        self.character.status = "physical"
        self.character.create_data = {}
        db.session.commit()
