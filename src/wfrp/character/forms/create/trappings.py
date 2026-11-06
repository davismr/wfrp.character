from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import RadioField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from wfrp.data.careers.data import CAREER_BY_CLASS
from wfrp.data.trappings.career_class import get_class_trappings

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class TrappingsFormView(BaseCreateFormView):

    def get_form(self):
        class TrappingsForm(BaseCreateForm):
            submit = SubmitField("Select Trappings")

        class ClassTrappingsForm(BaseCreateForm):
            pass

        class CareerTrappingsForm(BaseCreateForm):
            pass

        career_class = CAREER_BY_CLASS[self.character.career]
        class_trappings = get_class_trappings(career_class)
        career_trappings = self.character.career_data()[self.character.career][
            "trappings"
        ]
        for trapping in class_trappings:
            setattr(
                ClassTrappingsForm,
                trapping,
                RadioField(
                    trapping,
                    choices=[trapping],
                    default=trapping,
                    validators=[DataRequired()],
                ),
            )
        for trapping in career_trappings:
            setattr(
                CareerTrappingsForm,
                trapping,
                RadioField(
                    trapping,
                    choices=[trapping],
                    default=trapping,
                    validators=[DataRequired()],
                ),
            )
        setattr(TrappingsForm, "class_trappings", ClassTrappingsForm())
        setattr(TrappingsForm, "career_trappings", CareerTrappingsForm())
        form = TrappingsForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/trappings.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("create_name", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/trappings.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        self.character.status = "Name"
        self.character.create_data = {}
        db.session.commit()
