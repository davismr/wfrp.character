import pytest
from pyramid import testing

from wfrp.character.application import DBSession
from wfrp.character.application import dbsession
from wfrp.character.forms.edit_campaign import CampaignEditViews


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
