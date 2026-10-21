from flask import redirect
from flask import render_template
from flask import url_for
from wtforms import SubmitField

from wfrp.character.database import db
from wfrp.character.forms.create.base import BaseCreateForm
from wfrp.character.forms.create.base import BaseCreateFormView


class MagicForm(BaseCreateForm):
    submit = SubmitField("Select Magic")


class MagicFormView(BaseCreateFormView):

    def get_form(self):
        form = MagicForm()
        return form

    def get(self, id):
        self.get_character(id)
        form = self.get_form()
        return render_template(
            "create/magic.jinja2", form=form, character=self.character
        )

    def post(self, id):
        self.get_character(id)
        form = self.get_form()
        if form.validate_on_submit():
            self.update_character(form)
            next_url = url_for("create_trappings", id=self.character.id)
            return redirect(next_url)
        return render_template(
            "create/magic.jinja2", form=form, character=self.character
        )

    def update_character(self, form):
        self.character.status = "Trappings"
        self.character.create_data = {}
        db.session.commit()
