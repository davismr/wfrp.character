import os
import sys

from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging
from sqlalchemy import engine_from_config

from wfrp.character.models import Base
from wfrp.character.models import DBSession


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
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
