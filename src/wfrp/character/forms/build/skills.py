from flask import redirect
from flask import render_template
from flask import url_for
from wfrp.data.careers.data import CAREER_DATA
from wfrp.data.species import SPECIES_DATA
from wtforms import RadioField
from wtforms import SelectMultipleField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import CheckboxInput
from wtforms.widgets import ListWidget

from wfrp.character.database import db
from wfrp.character.forms.build.base import BaseBuildForm
from wfrp.character.forms.build.base import BaseBuildFormView


class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class SkillsFormView(BaseBuildFormView):

    def get_form(self):
        class SpeciesSkillsForm(BaseBuildForm):
            pass

        class CareerSkillsForm(BaseBuildForm):
            pass

        class SkillsForm(BaseBuildForm):
            submit = SubmitField("Select Advances")

        species_skills = SPECIES_DATA[self.character.species]["skills"]
        SpeciesSkillsForm.species_skills = MultiCheckboxField(
            "species_skills", choices=species_skills
        )
        career_skills = CAREER_DATA[self.character.career][self.character.career_title][
            "skills"
        ]
        for skill in career_skills:
            setattr(
                CareerSkillsForm,
                skill,
                RadioField(
                    skill,
                    choices=[0, 1, 2, 3],
                    default=0,
                    validators=[DataRequired()],
                ),
            )
        setattr(SkillsForm, "species_skills", SpeciesSkillsForm())
        setattr(SkillsForm, "career_skills", CareerSkillsForm())
        form = SkillsForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "build/skills.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("build_talents", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "build/skills.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        for skill in form.species_skills.data["species_skills"]:
            self.character.skills[skill] = 5
        career_skills = CAREER_DATA[self.character.career][self.character.career_title][
            "skills"
        ]
        for skill in career_skills:
            if form.career_skills.data[skill] != "0":
                self.character.skills[skill] = (
                    self.character.skills.setdefault(skill, 0)
                    + int(form.career_skills.data[skill]) * 5
                )
        self.character.status = "Talents"
        self.character.create_data = {}
        db.session.commit()
