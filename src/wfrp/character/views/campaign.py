import uuid

from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.campaign import Campaign
from wfrp.character.models.user import User


@view_defaults(renderer="wfrp.character:templates/campaign.pt")
class CampaignViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        if self.request.registry.settings.get("enable_auth"):
            if self.logged_in is None:
                raise HTTPUnauthorized
            else:
                self.user = (
                    self.request.dbsession.query(User)
                    .filter(User.email == self.logged_in)
                    .one()
                )
        self.campaign = (
            request.dbsession.query(Campaign)
            .filter(Campaign.id == uuid.UUID(request.matchdict["id"]))
            .one()
        )

    @view_config(route_name="campaign-view")
    def full_view(self):
        return {
            "campaign": self.campaign,
            "sessions": sorted(
                self.campaign.sessions, key=lambda x: x.session_date, reverse=True
            ),
        }
