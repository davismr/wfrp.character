import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.security import forget
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import NoResultFound

from wfrp.character.models.user import User
from wfrp.character.validators import confirm_delete_validator


@view_defaults(route_name="account")
class AccountPageViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        try:
            self.user = (
                self.request.dbsession.query(User)
                .filter(User.email == self.logged_in)
                .one()
            )
        except NoResultFound:
            raise HTTPUnauthorized

    def schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Update My Account",
        )
        schema.add(
            colander.SchemaNode(
                colander.Boolean(),
                widget=deform.widget.CheckboxWidget(),
                name="Subscribe",
                label="Subscribe to email updates",
                description=(
                    "Emails will be very infrequent, and your details will never be "
                    "passed to a third party."
                ),
                default=self.user.subscribed,
                missing=False,
            )
        )
        return schema

    def delete_schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Delete My Account",
        )
        if self.user.gamemaster_campaigns:
            campaign_schema = colander.SchemaNode(
                colander.Mapping(),
                title="Campaigns that will be deleted",
                name="campaigns",
            )
            for campaign in self.user.gamemaster_campaigns:
                if len(campaign.gamemasters) == 1:
                    campaign_schema.add(
                        colander.SchemaNode(
                            colander.String(),
                            title=campaign.get_display_title(),
                            widget=deform.widget.TextInputWidget(readonly=True),
                            missing="delete",
                        )
                    )
            if campaign_schema.children:
                schema.add(campaign_schema)
        if self.user.characters:
            character_schema = colander.SchemaNode(
                colander.Mapping(),
                title="Characters that will be deleted",
                name="characters",
            )
            for character in self.user.characters:
                character_schema.add(
                    colander.SchemaNode(
                        colander.String(),
                        title=character.get_display_title(),
                        widget=deform.widget.TextInputWidget(readonly=True),
                        missing="delete",
                    )
                )
            schema.add(character_schema)
        return schema

    @view_config(request_method="GET", renderer="wfrp.character:templates/account.pt")
    def get_view(self):
        schema = self.schema()
        delete_button = deform.Button(name="Delete Account", css_class="btn-danger")
        form = deform.Form(
            schema,
            buttons=("Update Account", delete_button),
        )
        html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    @view_config(
        request_method="POST", renderer="wfrp.character:templates/account_delete.pt"
    )
    def post_view(self):  # noqa: C901
        if "Update_Account" in self.request.POST:
            schema = self.schema()
            delete_button = deform.Button(name="Delete Account", css_class="btn-danger")
            form = deform.Form(
                schema,
                buttons=("Update Account", delete_button),
            )
        else:
            schema = self.delete_schema()
            schema.add(
                colander.SchemaNode(
                    colander.Boolean(),
                    widget=deform.widget.CheckboxWidget(),
                    name="confirm_delete",
                    title="Delete my account",
                    label="Confirm I want to delete my account",
                    validator=confirm_delete_validator,
                    missing=False,
                )
            )
            delete_button = deform.Button(
                name="Confirm Delete Account", css_class="btn-danger"
            )
            cancel_button = deform.Button(name="Cancel", css_class="btn-light")
            form = deform.Form(
                schema,
                buttons=(delete_button, cancel_button),
            )
        if "Cancel" in self.request.POST:
            return HTTPFound(location="/")
        elif (
            "Confirm_Delete_Account" in self.request.POST
            or "Update_Account" in self.request.POST
        ):
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if "Update_Account" in self.request.POST:
                    self.user.subscribed = captured.get("Subscribe")
                    if self.user.subscribed:
                        message = "You have subscribed to email updates"
                    else:
                        message = "You have unsubscribed"
                    self.request.session.flash(message, "error")
                else:
                    for character in self.user.characters:
                        self.request.dbsession.delete(character)
                    for campaign in self.user.gamemaster_campaigns:
                        if len(campaign.gamemasters) == 1:
                            self.request.dbsession.delete(campaign)
                    self.request.dbsession.delete(self.user)
                    forget(self.request)
                    message = "Your details and content have been deleted"
                    self.request.session.flash(message, "error")
                return HTTPFound(location="/")
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    def get_widget_resources(self, form):
        static_assets = form.get_widget_resources()
        static_assets["css"].append("deform:static/css/form.css")
        return static_assets
