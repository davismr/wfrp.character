from dataclasses import dataclass

from pyramid import testing
import pytest

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.experience import ExperienceGain
from wfrp.character.views.campaign_session import CampaignSessionViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_form_view(new_campaign):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="session-add")
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignSessionViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)


@pytest.mark.current
def test_form_view_character(new_campaign, new_character):
    new_campaign.characters.append(new_character)
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="session-add")
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignSessionViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)
    assert f'name="{str(new_character.id)}"' in response["form"]


@pytest.mark.views
def test_form_valid(new_campaign):
    payload = {
        "campaign_session": {
            "title": "Our Campaign Session",
            "date": {"date": "2024-12-13"},
            "summary": "<p>The summary</p>",
        },
        "Add_Campaign_Session": "Add_Campaign_Session",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="session-add")
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignSessionViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == (f"http://example.com/campaign/{new_campaign.id}/view")


@pytest.mark.current
def test_form_valid_character(new_campaign, new_character):
    DBSession.query(ExperienceGain).delete()
    new_campaign.characters.append(new_character)
    payload = {
        "campaign_session": {
            "title": "Our Campaign Session",
            "date": {"date": "2024-12-13"},
            "summary": "<p>The summary</p>",
            "characters": {str(new_character.id): "50"},
        },
        "Add_Campaign_Session": "Add_Campaign_Session",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="session-add")
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignSessionViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == (f"http://example.com/campaign/{new_campaign.id}/view")
    results = request.dbsession.query(ExperienceGain).all()
    assert len(results) == 1
    experience_gain = results[0]
    assert experience_gain.amount == 50
    assert experience_gain.campaign_session.title == "Our Campaign Session"
