import pytest
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPUnauthorized


@pytest.mark.edit
def test_not_found(testapp):
    with pytest.raises(HTTPNotFound) as error:
        testapp.get("/foobar")
    assert str(error.value) == "/foobar"


# @pytest.mark.edit
# def test_unauthorised(testapp):
#     with pytest.raises(HTTPUnauthorized) as error:
#         testapp.get("/account", status=401)
#     assert str(error.value).startswith(
#         "This server could not verify that you are authorized to access the document "
#         "you requested."
#     )


@pytest.mark.edit
def test_unauthorised(testapp):
    response = testapp.get("/account", status=401)
    breakpoint()
    assert str(error.value).startswith(
        "This server could not verify that you are authorized to access the document "
        "you requested."
    )
