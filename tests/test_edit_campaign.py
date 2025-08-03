import pytest
from pyramid import testing

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.models.campaign import Campaign
from wfrp.character.views.edit_campaign import CampaignEditViews


@pytest.mark.edit
def test_form_view(campaign_factory):
    new_campaign = campaign_factory()
    DBSession.add(new_campaign)
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignEditViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.campaign
def test_form_view_new(testapp):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    view = CampaignEditViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response
    assert "Rough Nights and Hard Days" in response["form"]


@pytest.mark.campaign
def test_submit(testapp):
    DBSession.query(Campaign).delete()
    request = testing.DummyRequest(
        post={
            "campaign_name": "My Awesome Campaign",
            "expansions": ["rough_nights", "sea_of_claws"],
            "Save": "Save",
        }
    )
    request.dbsession = dbsession(request)
    campaigns = request.dbsession.query(Campaign).all()
    assert len(campaigns) == 0
    view = CampaignEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == "/"
    campaigns = request.dbsession.query(Campaign).all()
    assert len(campaigns) == 1
    assert campaigns[0].name == "My Awesome Campaign"
    assert campaigns[0].expansions.sort() == ["rough_nights", "sea_of_claws"].sort()


@pytest.mark.campaign
def test_campaign_delete(new_campaign):
    num_campaigns = DBSession.query(Campaign).count()
    request = testing.DummyRequest(
        post={"confirm_delete": "true", "Confirm_delete": "Confirm_delete"}
    )
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(new_campaign.id)}
    view = CampaignEditViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == "/"
    assert DBSession.query(Campaign).count() == num_campaigns - 1
