from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.data.constants import Characteristics
from wfrp.data.dice import roll_2d10
from wfrp.data.species import SPECIES_DATA

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class CharacteristicsFormView(BaseCreateFormView):

    def initialise_form(self):
        if not self.character.create_data:
            for characteristic in Characteristics:
                die_roll = roll_2d10()
                self.character.create_data[characteristic.name] = die_roll
            db.session.commit()

    def get_form(self):
        class CharacteristicsForm(BaseCreateForm):
            accept = SubmitField("Accept Characteristics")
            rearrange = SubmitField("Rearrange Characteristics")
            reroll = SubmitField("Reroll Characteristics")

        self.initialise_form()
        all_rolls = sorted(list(self.character.create_data.values()))
        for characteristic in Characteristics:
            setattr(
                CharacteristicsForm,
                characteristic.name,
                RadioField(
                    characteristic.name,
                    choices=all_rolls,
                    default=self.character.create_data[characteristic.name],
                    validators=[DataRequired()],
                ),
            )
        form = CharacteristicsForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/characteristics.jinja2",
            form=form,
            character=self.character,
            species_modifiers=SPECIES_DATA[self.character.species]["characteristics"],
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form.data)
            next_url = url_for("create_skills", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/characteristics.jinja2",
            form=form,
            character=self.character,
            species_modifiers=SPECIES_DATA[self.character.species]["characteristics"],
        )

    def update_character(self, data):
        if data["reroll"]:
            raise NotImplementedError
        for characteristic in Characteristics:
            characteristic_lower = characteristic.value.lower().replace(" ", "_")
            species_bonus = SPECIES_DATA[self.character.species]["characteristics"][
                characteristic.name
            ]
            if data["accept"]:
                die_roll = self.character.create_data[characteristic.name]
            elif data["rearrange"]:
                die_roll = data[characteristic.name]
            setattr(
                self.character,
                f"{characteristic_lower}_initial",
                die_roll + species_bonus,
            )
        self.character.status = "skills"
        self.character.create_data = {}
        db.session.commit()
