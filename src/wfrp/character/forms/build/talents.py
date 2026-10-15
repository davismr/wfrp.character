from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wtforms import RadioField
from wfrp.character.database import db
from wfrp.character.forms.build.base import BaseBuildFormView
from wfrp.character.forms.build.base import BaseBuildForm
from wfrp.data.species import SPECIES_DATA
from wfrp.data.tables.talents import get_random_talent
from wfrp.data.dice import roll_d100
from wfrp.data.careers.data import CAREER_DATA


class TalentsFormView(BaseBuildFormView):
    # def __init__(self):
    #     breakpoint()
    #     pass

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
        class SpeciesTalentsForm(BaseBuildForm):
            pass

        class CareerTalentsForm(BaseBuildForm):
            pass

        class TalentsForm(BaseBuildForm):
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
            "build/talents.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("build_magic", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "build/talents.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        for talent in self.character.create_data["talents"]:
            self.character.talents[talent] = 1
        self.character.talents[form.career_talents.data["career_talents"]] = 1
        self.character.status = "Magic"
        self.character.create_data = {}
        db.session.commit()
