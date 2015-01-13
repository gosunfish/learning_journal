import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models import (
    DBSession,
    MyModel,
    Base,
    Entry
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = MyModel(name='one', value=1)
        DBSession.add(model)
    with transaction.manager:
        model = Entry(title='Time Travel', body='The earth is neither round nor flat. It is actually shaped like ribbon candy.')
        DBSession.add(model)
        model = Entry(title='Good Men', body='Now is the time for all good men to come to the aid of their country.')
        DBSession.add(model)
        model = Entry(title='Miranda', body='I have the right to remain silent. Anything I say can and will be used against me.')
        DBSession.add(model)
        model = Entry(title='Surgeon General', body='Smoking causes cancer.')
        DBSession.add(model)
