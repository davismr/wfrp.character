from pyramid import testing
import pytest

from wfrp.character.views.homepage import HomePageViews


@pytest.mark.package
def test_passing_view(session_db):
    view = HomePageViews(testing.DummyRequest())
    response = view.homepage_get_view()
    assert response.status_code == 200
    assert "Create new character" in response.text
