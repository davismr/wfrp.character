import uuid
from datetime import datetime
from datetime import timezone

from sqlalchemy import JSON
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import event
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.schema import ForeignKey

from wfrp.character.application import Base


class Campaign(Base):
    __tablename__ = "campaign"
    uid = Column(Integer, primary_key=True)
    uuid = Column(Text, default=str(uuid.uuid4()))
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    modified = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = Column(Integer, ForeignKey("user.uid"))
    name = Column(Text)
    expansions = Column(MutableList.as_mutable(JSON), default=[])

    def get_display_title(self):
        return self.name


@event.listens_for(Campaign, "before_update")
def campaign_before_update(mapper, connection, target):
    target.modified = datetime.now(timezone.utc)
