from datetime import datetime
from datetime import timezone

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import event

from wfrp.character.application import Base


class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    name = Column(Text)
    given_name = Column(Text)
    family_name = Column(Text)
    email = Column(Text)


@event.listens_for(User, "before_update")
def user_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)
