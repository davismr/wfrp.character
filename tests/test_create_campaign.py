import uuid
from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.application import dbsession
from wfrp.character.models.campaign import Campaign
from wfrp.character.views.create_character.campaign import CampaignViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_get_view(new_character):
    request = testing.DummyRequest(path="campaign")
    request.dbsession = dbsession(request)
    new_campaign = Campaign()
    new_campaign.name = "My Campaign"
    request.dbsession.add(new_campaign)
    request.matched_route = DummyRoute(name="campaign")
    request.matchdict = {"id": str(new_character.id)}
    view = CampaignViews(request)
    response = view.form_view()
    assert "form" in response
    assert "My Campaign" in response["form"]
    assert "Choose campaign" in response["form"]


@pytest.mark.create
def test_submit_view(new_character, new_campaign):
    request = testing.DummyRequest(
        post={
            "campaign": {"campaign": str(new_campaign.id)},
            "Choose_Campaign": "Choose_Campaign",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="campaign")
    request.matchdict = {"id": str(new_character.id)}
    view = CampaignViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.campaign.id == new_campaign.id


@pytest.mark.create
def test_submit_empty(new_character, new_campaign):
    request = testing.DummyRequest(
        post={"campaign": {"campaign": ""}, "Choose_Campaign": "Choose_Campaign"}
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="campaign")
    request.matchdict = {"id": str(new_character.id)}
    view = CampaignViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.campaign is None


@pytest.mark.create
def test_submit_invalid_campaign(new_character, new_campaign):
    request = testing.DummyRequest(
        post={
            "campaign": {"campaign": str(uuid.uuid4())},
            "Choose_Campaign": "Choose_Campaign",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="campaign")
    request.matchdict = {"id": str(new_character.id)}
    view = CampaignViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "is not one of" in response["form"]
