import pytest
from pyramid import testing

from wfrp.character.views.homepage import HomePageViews


@pytest.mark.package
def test_passing_view(session_db):
    view = HomePageViews(testing.DummyRequest())
    response = view.homepage_get_view()
    assert response == {}
