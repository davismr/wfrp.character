import uuid

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.validators import confirm_delete_validator
from wfrp.character.validators import is_user_found
from wfrp.character.views.base_view import BaseView


@view_defaults(
    route_name="character-transfer",
    renderer="wfrp.character:templates/forms/base_form.pt",
)
class TransferViews(BaseView):
    def initialise_form(self):
        all_actions = [
            "Delete_Character",
            "Confirm_Delete",
            "Transfer_Character",
            "Confirm_Transfer",
        ]
        button = set(self.request.POST).intersection(all_actions)
        elements = button.pop().split("_")
        if elements[0] == "Confirm":
            confirm = True
            action = elements[1].lower()
        else:
            confirm = False
            action = elements[0].lower()
        return {"action": action, "confirm": confirm}

    def schema(self, data):
        action = data["action"]
        if action == "":
            title = "Transfer or Delete Character"
        else:
            title = f"{action.title()} Character"
        schema = colander.SchemaNode(colander.Mapping(), title=title)
        if action == "transfer":
            transfer_schema = colander.SchemaNode(
                colander.Mapping(),
                name="transfer_character",
                description="Transfer the character to another user",
            )
            transfer_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name="transfer_user",
                    widget=deform.widget.TextInputWidget(),
                    validator=is_user_found,
                    missing="",
                )
            )
            schema.add(transfer_schema)
        if data["action"]:
            schema.add(
                colander.SchemaNode(
                    colander.Boolean(),
                    widget=deform.widget.CheckboxWidget(),
                    name=f"confirm_{action}",
                    title=f"{action.title()} my character",
                    label=f"Confirm I want to {action} my character",
                    validator=confirm_delete_validator,
                )
            )
        return schema

    @view_config(request_method="GET")
    def get_view(self):
        data = {"action": "", "confirm": False}
        schema = self.schema(data)
        form = deform.Form(
            schema,
            buttons=("Transfer Character", "Delete Character"),
        )
        html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    @view_config(request_method="POST")
    def post_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        action = data["action"]
        form = deform.Form(
            schema,
            buttons=(f"Confirm {action.title()}",),
        )
        if data["confirm"] is True:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if action == "delete":
                    self.request.dbsession.delete(self.character)
                    self.request.session.flash(
                        "Your character has been deleted", "success"
                    )
                elif action == "transfer":
                    self.character.user_id = uuid.UUID(
                        captured["transfer_character"]["transfer_user"]
                    )
                    self.request.session.flash(
                        "Your character has been transferred", "success"
                    )
                return HTTPFound(location="/")
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
