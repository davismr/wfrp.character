import uuid

from colander import Email
from colander import Invalid
from sqlalchemy import exists

from wfrp.character.application import DBSession
from wfrp.character.models.user import User


def confirm_delete_validator(node, value):
    if not value:
        object_type = node.title.split(" ")[-1]
        raise Invalid(
            node, f"You have to confirm that you want to delete your {object_type}"
        )


def is_user_found(node, value):
    """Checks whether value is a uuid or email and maps to a user."""
    try:
        user_id = uuid.UUID(value, version=4)
    except ValueError:
        pass
    else:
        user_exists = DBSession.query(exists().where(User.id == user_id)).scalar()
        if user_exists is False:
            raise Invalid(node, "User with this id not found")
        return
    Email("This is not a valid email or user id")(node, value)
    user_exists = DBSession.query(exists().where(User.email == value)).scalar()
    if user_exists is False:
        raise Invalid(node, "User with this email not found")
