from flask import redirect
from flask import render_template
from flask import url_for
from wfrp.data.careers.data import CAREER_DATA
from wfrp.data.dice import roll_d100
from wfrp.data.species import SPECIES_DATA
from wfrp.data.tables.talents import get_random_talent
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class TalentsFormView(BaseCreateFormView):

    def initialise_form(self):
        if not self.character.create_data:
            talents = SPECIES_DATA[self.character.species]["talents"]
            while len(talents) < 5:
                new_talent = get_random_talent(roll_d100())
                if new_talent not in talents:
                    talents.append(new_talent)
            self.character.create_data["talents"] = talents
            db.session.commit()
        pass

    def get_form(self):
        class SpeciesTalentsForm(BaseCreateForm):
            pass

        class CareerTalentsForm(BaseCreateForm):
            pass

        class TalentsForm(BaseCreateForm):
            submit = SubmitField("Select Talents")

        self.initialise_form()
        for talent in self.character.create_data["talents"]:
            setattr(
                SpeciesTalentsForm,
                talent,
                RadioField(
                    talent,
                    choices=[talent],
                    default=talent,
                    validators=[DataRequired()],
                ),
            )
        career_talents = CAREER_DATA[self.character.career][
            self.character.career_title
        ]["talents"]
        setattr(
            CareerTalentsForm,
            "career_talents",
            RadioField(
                "Career Talents",
                choices=career_talents,
                validators=[DataRequired()],
            ),
        )
        setattr(TalentsForm, "species_talents", SpeciesTalentsForm())
        setattr(TalentsForm, "career_talents", CareerTalentsForm())
        form = TalentsForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/talents.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("create_magic", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/talents.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        for talent in self.character.create_data["talents"]:
            self.character.talents[talent] = 1
        self.character.talents[form.career_talents.data["career_talents"]] = 1
        self.character.status = "Magic"
        self.character.create_data = {}
        db.session.commit()
