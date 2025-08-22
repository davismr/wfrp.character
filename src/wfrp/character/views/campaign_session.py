import uuid

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.campaign import Campaign
from wfrp.character.models.campaign import CampaignSession
from wfrp.character.models.experience import ExperienceGain
from wfrp.character.views.base_view import BaseView


@view_defaults(renderer="wfrp.character:templates/forms/session.pt")
class CampaignSessionViews(BaseView):
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        id = request.matchdict["id"]
        if self.request.matched_route.name == "session-add":
            self.edit = False
            self.campaign = (
                request.dbsession.query(Campaign)
                .filter(Campaign.id == uuid.UUID(id))
                .one()
            )
        else:
            self.edit = True
            self.campaign_session = (
                request.dbsession.query(CampaignSession)
                .filter(CampaignSession.id == uuid.UUID(id))
                .one()
            )
            self.campaign = self.campaign_session.campaign

    def schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Campaign Session")
        campaign_schema = colander.SchemaNode(
            colander.Mapping(),
            name="campaign_session",
        )
        campaign_schema.add(
            colander.SchemaNode(
                colander.String(),
                title="Title",
                widget=deform.widget.TextInputWidget(),
                name="title",
                default=self.campaign_session.title if self.edit else "",
            )
        )
        campaign_schema.add(
            colander.SchemaNode(
                colander.Date(),
                title="Session Date",
                widget=deform.widget.DateInputWidget(),
                name="date",
                default=self.campaign_session.session_date if self.edit else "",
            )
        )
        campaign_schema.add(
            colander.SchemaNode(
                colander.String(),
                title="Session Summary",
                validator=colander.Length(max=100),
                widget=deform.widget.RichTextWidget(),
                name="summary",
                default=self.campaign_session.summary if self.edit else "",
            )
        )
        if self.edit is False:
            character_schema = colander.SchemaNode(
                colander.Mapping(),
                name="characters",
            )
            for character in self.campaign.characters:
                character_schema.add(
                    colander.SchemaNode(
                        colander.Integer(),
                        title=character.get_display_title(),
                        widget=deform.widget.TextInputWidget(),
                        name=str(character.id),
                        missing=0,
                    )
                )
            campaign_schema.add(character_schema)
        schema.add(campaign_schema)
        return schema

    @view_config(route_name="session-add")
    @view_config(route_name="session-edit")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(
            schema,
            buttons=("Add Campaign Session",),
        )
        if "Add_Campaign_Session" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if self.edit:
                    self.campaign_session.title = captured["campaign_session"]["title"]
                    self.campaign_session.session_date = captured["campaign_session"][
                        "date"
                    ]
                    self.campaign_session.summary = captured["campaign_session"][
                        "summary"
                    ]
                else:
                    session = CampaignSession(
                        campaign_id=self.campaign.id,
                        title=captured["campaign_session"]["title"],
                        session_date=captured["campaign_session"]["date"],
                        summary=captured["campaign_session"]["summary"],
                    )
                    self.request.dbsession.add(session)
                if self.edit is False:
                    for character, amount in captured["campaign_session"][
                        "characters"
                    ].items():
                        if amount != 0:
                            experience = ExperienceGain(
                                character_id=uuid.UUID(character),
                                amount=amount,
                                campaign_session=session,
                            )
                            self.request.dbsession.add(experience)
                url = self.request.route_url("campaign_view", id=self.campaign.id)
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
