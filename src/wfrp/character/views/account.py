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
            breakpoint()
            raise HTTPUnauthorized

    def schema(self):
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Delete My Account",
        )
        return schema

    @view_config(request_method="GET", renderer="wfrp.character:templates/account.pt")
    def get_view(self):
        schema = self.schema()
        form = deform.Form(
            schema,
            buttons=("Delete Account",),
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
    def post_view(self):
        schema = self.schema()
        schema.add(
            colander.SchemaNode(
                colander.Boolean(),
                widget=deform.widget.CheckboxWidget(),
                name="confirm_delete",
                title="Delete my account",
                label="Confirm I want to delete my account",
                validator=confirm_delete_validator,
            )
        )
        form = deform.Form(
            schema,
            buttons=("Confirm Account", "Cancel"),
        )
        if "Cancel" in self.request.POST:
            return HTTPFound(location="/")
        if "Confirm_Account" in self.request.POST:
            try:
                form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                for character in self.user.characters:
                    self.request.dbsession.delete(character)
                self.request.dbsession.delete(self.user)
                forget(self.request)
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
