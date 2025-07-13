import pytest
from pyramid import testing

from wfrp.character.application import dbsession
from wfrp.character.forms.edit_campaign import CampaignEditViews
from wfrp.character.models.campaign import Campaign


@pytest.mark.campaign
def test_form_view_new(testapp):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    view = CampaignEditViews(request)
    response = view.form_view_new()
    assert isinstance(response, dict)
    assert "form" in response
    assert "Rough Nights and Hard Days" in response["form"]


@pytest.mark.campaign
def test_submit(testapp):
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
    response = view.form_view_new()
    assert response.status_code == 302
    assert response.location == "/"
    campaigns = request.dbsession.query(Campaign).all()
    assert len(campaigns) == 1
    assert campaigns[0].name == "My Awesome Campaign"
    assert campaigns[0].expansions.sort() == ["rough_nights", "sea_of_claws"].sort()
