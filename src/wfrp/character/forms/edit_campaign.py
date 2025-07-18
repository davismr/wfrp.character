import uuid

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy import exists

from wfrp.character.data.expansions import EXPANSIONS
from wfrp.character.models.campaign import Campaign


@view_defaults(route_name="campaign_edit")
class CampaignEditViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        if "id" in request.matchdict:
            self.campaign = (
                request.dbsession.query(Campaign)
                .filter(Campaign.id == uuid.UUID(request.matchdict["id"]))
                .one()
            )
        else:
            self.campaign = Campaign()

    def schema(self):
        if self.campaign.id:
            schema = colander.SchemaNode(
                colander.Mapping(), title=f"Edit {self.campaign.get_display_title()}"
            )
        else:
            schema = colander.SchemaNode(colander.Mapping(), title="Create campaign")
        schema.add(
            colander.SchemaNode(
                colander.String(),
                name="campaign_name",
                widget=deform.widget.TextInputWidget(),
                validator=colander.Length(max=100),
                default=self.campaign.name or "",
            )
        )
        choices = [
            (expansion[0], expansion[1]["title"]) for expansion in EXPANSIONS.items()
        ]
        schema.add(
            colander.SchemaNode(
                colander.Set(),
                name="expansions",
                widget=deform.widget.CheckboxChoiceWidget(values=choices),
                validator=colander.Length(min=0),
                missing=[],
                default=self.campaign.expansions,
            )
        )
        return schema

    @view_config(
        route_name="campaign_new", renderer="wfrp.character:templates/campaign_form.pt"
    )
    @view_config(
        route_name="campaign_edit", renderer="wfrp.character:templates/campaign_form.pt"
    )
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Save",))
        if "Save" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.campaign.name = captured.get("campaign_name")
                self.campaign.expansions = list(captured.get("expansions"))
                if (
                    self.request.dbsession.query(
                        exists().where(Campaign.id == self.campaign.id)
                    ).scalar()
                    is False
                ):
                    self.request.dbsession.add(self.campaign)
                return HTTPFound(location="/")
        else:
            html = form.render()
        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    def get_widget_resources(self, form):
        static_assets = form.get_widget_resources()
        static_assets["css"].append("deform:static/css/form.css")
        return static_assets
