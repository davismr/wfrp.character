from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import SubmitField

from wfrp.character.forms.build.base import BaseBuildFormView, BaseBuildForm
from wfrp.character.database import db


class TrappingsForm(BaseBuildForm):
    submit = SubmitField("Select Trappings")


class TrappingsFormView(BaseBuildFormView):

    def get_form(self):
        form = TrappingsForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "build/trappings.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("build_name", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "build/trappings.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        self.character.status = "Name"
        self.character.create_data = {}
        db.session.commit()
