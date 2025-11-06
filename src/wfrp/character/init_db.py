import logging
import os
import sys

from dotenv import load_dotenv
from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging
from sqlalchemy import engine_from_config

from wfrp.character.application import DBSession
from wfrp.character.models.campaign import Campaign
from wfrp.character.models.campaign import CampaignSession
from wfrp.character.models.character import Character
from wfrp.character.models.experience import ExperienceCost
from wfrp.character.models.experience import ExperienceGain
from wfrp.character.models.user import User

load_dotenv()

logger = logging.getLogger(__name__)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print("usage: %s <config_uri>\n" '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    logger.critical(os.environ.keys())
    print(os.environ.keys())
    print(os.getenv("RAILWAY_PUBLIC_DOMAIN"))
    print(os.getenv("RAILWAY_PUBLIC_DOMAIN"))
    settings["sqlalchemy.url"] = os.getenv("DATABASE_URL")
    if settings["sqlalchemy.url"] is None:
        raise Exception("Can not find env var")
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Campaign.metadata.create_all(engine)
    CampaignSession.metadata.create_all(engine)
    Character.metadata.create_all(engine)
    ExperienceCost.metadata.create_all(engine)
    ExperienceGain.metadata.create_all(engine)
    User.metadata.create_all(engine)
