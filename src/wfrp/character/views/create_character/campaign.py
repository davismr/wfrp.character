import uuid

import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.campaign import Campaign
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class CampaignViews(BaseCreateView):
    def initialise_form(self):
        if self.character.user:
            campaigns = self.character.user.player_campaigns
        else:
            campaigns = self.request.dbsession.query(Campaign).all()
        campaign_list = [("", "No campaign")]
        for campaign in campaigns:
            campaign_list.append((str(campaign.id), campaign.get_display_title()))
        return {"campaign_list": campaign_list}

    def schema(self, data):
        schema = colander.SchemaNode(colander.Mapping(), title="Character Campaign")
        campaign_schema = colander.SchemaNode(
            colander.Mapping(),
            name="campaign",
        )
        campaign_schema.add(
            colander.SchemaNode(
                colander.String(),
                name="campaign",
                validator=colander.OneOf([x[0] for x in data["campaign_list"]]),
                widget=deform.widget.RadioChoiceWidget(values=data["campaign_list"]),
                description="Select the campaign the character belongs to",
                default="",
                missing="",
            )
        )
        schema.add(campaign_schema)
        return schema

    @view_config(route_name="campaign")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema,
            buttons=("Choose Campaign",),
        )
        if "Choose_Campaign" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if captured["campaign"]["campaign"]:
                    campaign = (
                        self.request.dbsession.query(Campaign)
                        .filter(
                            Campaign.id == uuid.UUID(captured["campaign"]["campaign"])
                        )
                        .one()
                    )
                    self.character.campaign = campaign
                url = self.request.route_url("expansions", id=self.character.id)
                self.character.status = {"expansions": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
