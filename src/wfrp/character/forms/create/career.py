from flask import redirect
from flask import render_template
from flask import url_for
from wfrp.data.careers.data import CAREER_BY_CLASS
from wfrp.data.careers.data import CAREER_DATA
from wfrp.data.dice import roll_d100
from wfrp.data.tables.careers import get_career
from wfrp.data.tables.careers import get_career_list
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class CareerForm(BaseCreateForm):
    career = RadioField("Career", validators=[DataRequired()])
    submit = SubmitField("Select Career")


class CareerFormView(BaseCreateFormView):

    def initialise_form(self):
        if not self.character.create_data:
            die_roll = roll_d100()
            self.character.create_data = {
                "die_roll": die_roll,
                "career": get_career(self.character.species, die_roll),
            }
            db.session.commit()

    def get_form(self):
        self.initialise_form()
        form = CareerForm(career=self.character.create_data["career"])
        form.career.choices = list(get_career_list(self.character.species).values())
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/career.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form.data)
            next_url = url_for("create_religion", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/career.jinja2", form=form, character=self.character
        )

    def update_character(self, data):
        career_data = CAREER_DATA[data["career"]]
        self.character.career = data["career"]
        self.character.career_class = CAREER_BY_CLASS[data["career"]]
        career_title = list(career_data.keys())[1]
        self.character.career_title = career_title
        self.character.career_path.append(career_title)
        self.character.career_tier = career_data[career_title]["status"]["tier"]
        self.character.career_standing = career_data[career_title]["status"]["standing"]
        self.character.status = "Religion"
        self.character.create_data = {}
        db.session.commit()
