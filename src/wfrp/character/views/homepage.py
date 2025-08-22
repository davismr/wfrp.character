from pyramid.security import forget
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import NoResultFound

from wfrp.character.models.campaign import Campaign
from wfrp.character.models.character import Character
from wfrp.character.models.user import User


@view_defaults(route_name="homepage")
class HomePageViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(
        request_method="GET", renderer="wfrp.character:templates/homepage/homepage.pt"
    )
    def get_view(self):
        campaign_list = {}
        gamemaster_campaigns_list = {}
        character_list = {}
        if self.request.registry.settings.get("enable_auth"):
            if self.logged_in is None:
                return {"gamemaster_campaigns": {}, "campaigns": {}, "characters": {}}
            try:
                user = (
                    self.request.dbsession.query(User)
                    .filter(User.email == self.logged_in)
                    .one()
                )
            except NoResultFound:
                forget(self.request)
                return {"gamemaster_campaigns": {}, "campaigns": {}, "characters": {}}
            campaigns = user.player_campaigns
            gamemaster_campaigns = user.gamemaster_campaigns
            characters = (
                self.request.dbsession.query(Character)
                .filter(Character.user_id == user.id)
                .all()
            )
        else:
            campaigns = self.request.dbsession.query(Campaign).all()
            gamemaster_campaigns = {}
            characters = self.request.dbsession.query(Character).all()
        for campaign in campaigns:
            url = self.request.route_url("campaign_view", id=campaign.id)
            campaign_list[url] = campaign.get_display_title()
        for campaign in gamemaster_campaigns:
            url = self.request.route_url("campaign_view", id=campaign.id)
            gamemaster_campaigns_list[url] = campaign.get_display_title()
        for character in characters:
            url = self.request.route_url("character_summary", id=character.id)
            character_list[url] = character.get_display_title()
        return {
            "gamemaster_campaigns": gamemaster_campaigns_list,
            "campaigns": campaign_list,
            "characters": character_list,
        }
