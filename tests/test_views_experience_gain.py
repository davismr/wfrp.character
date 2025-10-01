from pyramid import testing
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.experience_gain import ExperienceGainViews


@pytest.mark.views
def test_form_view(complete_character):
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceGainViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)


@pytest.mark.views
def test_form_valid(complete_character):
    payload = {
        "experience_gain": {"amount": "40", "reason": "Give some experience"},
        "Give_Experience": "Give_Experience",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceGainViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == (
        f"http://example.com/character/{complete_character.id}/summary"
    )
    assert complete_character.experience == 40


@pytest.mark.views
def test_form_negative_amount(complete_character):
    complete_character.experience = 50
    payload = {
        "experience_gain": {"amount": "-40", "reason": "Give some experience"},
        "Give_Experience": "Give_Experience",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceGainViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert response.location == (
        f"http://example.com/character/{complete_character.id}/summary"
    )
    assert complete_character.experience == 10


@pytest.mark.views
def test_form_text_amount(complete_character):
    payload = {
        "experience_gain": {"amount": "broken", "reason": "Give some experience"},
        "Give_Experience": "Give_Experience",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceGainViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert '"broken" is not a number' in response["form"]


@pytest.mark.views
def test_form_missing_amount(complete_character):
    payload = {
        "experience_gain": {"reason": "Give some experience"},
        "Give_Experience": "Give_Experience",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matchdict = {"id": str(complete_character.id)}
    view = ExperienceGainViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "There was a problem with your submission" in response["form"]
