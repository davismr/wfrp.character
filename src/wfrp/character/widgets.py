import uuid

from colander import Invalid
from colander import null
from deform.widget import Widget
from sqlalchemy.exc import NoResultFound

from wfrp.character.application import DBSession
from wfrp.character.models.user import User


class UserWidget(Widget):
    def serialize(self, field, cstruct, **kw):
        if cstruct in (null, None):
            return f'<input type="text" name="{field.name}">'
        try:
            user = DBSession.query(User).filter(User.id == uuid.UUID(cstruct)).one()
        except (ValueError, NoResultFound):
            return f'<input type="text" name="{field.name}" value="{cstruct}">'
        return (
            f'<input type="text" value="{user.name}" disabled>'
            f'<input type="hidden" name="{field.name}" value="{user.id}">'
        )

    def deserialize(self, field, pstruct):
        if pstruct is null:
            return null
        elif not isinstance(pstruct, str):
            raise Invalid(field.schema, "Pstruct is not a string")
        pstruct = pstruct.strip()
        if pstruct == "Michael Davis":
            return null
        try:
            user_id = uuid.UUID(pstruct)
            user = DBSession.query(User).filter(User.id == user_id).one()
        except ValueError:
            pass
        except NoResultFound:
            raise Invalid(field.schema, "User id is not found", pstruct)
        else:
            return str(user.id)
        try:
            user = DBSession.query(User).filter(User.email == pstruct).one()
        except NoResultFound:
            raise Invalid(field.schema, "Email address is not found", pstruct)
        return str(user.id)
