from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.update_character import UpdateCharacterViews


@pytest.mark.create
def test_get_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest()
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "form" in response


@pytest.mark.create
def test_submit_wounds_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest(
        post={
            "__formid__": "wounds_form",
            "Update_Wounds": "Update_Wounds",
            "wounds": {
                "wounds": "2 wounds, bleeding",
            },
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.wounds_current == "2 wounds, bleeding"


@pytest.mark.create
def test_submit_psychology_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest(
        post={
            "__formid__": "psychology_form",
            "Update_Psychology": "Update_Psychology",
            "psychology": {
                "psychology": "Prejudice (Elves)",
            },
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.psychology == "Prejudice (Elves)"


@pytest.mark.create
def test_submit_corruption_view(new_character):
    new_character.status = "complete"
    request = testing.DummyRequest(
        post={
            "__formid__": "corruption_form",
            "Update_Corruption": "Update_Corruption",
            "corruption": {
                "corruption": "2 corruption points",
            },
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.corruption == "2 corruption points"


@pytest.mark.create
def test_submit_ambitions_view(new_character):
    new_character.status = "complete"
    new_character.short_term_ambition = "Have breakfast"
    new_character.long_term_ambition = "Have second breakfast"
    request = testing.DummyRequest(
        post={
            "__formid__": "ambitions_form",
            "Update_Ambitions": "Update_Ambitions",
            "ambition": {
                "long_term_ambition": "Destroy the ring",
                "short_term_ambition": "Reach Bree",
            },
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.short_term_ambition == "Reach Bree"
    assert new_character.long_term_ambition == "Destroy the ring"


@pytest.mark.create
def test_submit_wealth_view(new_character):
    new_character.status = "complete"
    new_character.wealth = {"gold crowns": 5}
    request = testing.DummyRequest(
        post={
            "__formid__": "wealth_form",
            "Update_Wealth": "Update_Wealth",
            "wealth": {
                "gold_crowns": "0",
                "brass_pennies": "15",
            },
        }
    )
    request.matchdict = {"id": str(new_character.id)}
    request.dbsession = dbsession(request)
    view = UpdateCharacterViews(request)
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.brass_pennies == 15
    assert new_character.silver_shillings == 0
    assert new_character.gold_crowns == 0
