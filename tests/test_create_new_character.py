import pytest
from pyramid import testing

from wfrp.character.forms.create.new_character import NewCharacterViews


@pytest.mark.create
def test_get_view(testapp):
    view = NewCharacterViews(testing.DummyRequest())
    response = view.get_view()
    assert response.status_code == 302
    assert "Location" in response.headers
