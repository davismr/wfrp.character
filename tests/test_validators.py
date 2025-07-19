import uuid

import colander
import pytest
from colander import Invalid

from wfrp.character.application import DBSession
from wfrp.character.models.user import User
from wfrp.character.validators import is_user_found


@pytest.mark.forms
def test_invalid(testapp):
    node = colander.SchemaNode(colander.String(), name="valid_user")
    with pytest.raises(Invalid) as error:
        is_user_found(node, "invalid_string")
    assert error.value.node.name == "valid_user"
    assert error.value.msg == "This is not a valid email or user id"
    with pytest.raises(Invalid) as error:
        is_user_found(node, str(uuid.uuid4()))
    assert error.value.msg == "User with this id not found"
    with pytest.raises(Invalid) as error:
        is_user_found(node, "invalid@email")
    assert error.value.msg == "User with this email not found"


@pytest.mark.forms
def test_valid(testapp):
    node = colander.SchemaNode(colander.String(), name="valid_user")
    new_user = User()
    new_user.email = "user@here.com"
    DBSession.add(new_user)
    new_user = DBSession.query(User).filter_by(email="user@here.com").first()
    is_user_found(node, new_user.email)
    is_user_found(node, str(new_user.id))
