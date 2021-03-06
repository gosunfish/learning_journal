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
    Base,
    Entry,
    User,
    )

from cryptacular.bcrypt import BCRYPTPasswordManager as Manager

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
    if 'DATABASE_URL' in os.environ:
        settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = Entry(title='Time Travel', body='The earth is neither round nor flat. It is actually shaped like ribbon candy.')
        DBSession.add(model)
        model = Entry(title='Good Men', body='Now is the time for all good men to come to the aid of their country.')
        DBSession.add(model)
        model = Entry(title='Miranda', body='I have the right to remain silent. Anything I say can and will be used against me.')
        DBSession.add(model)
        model = Entry(title='Surgeon General', body='Smoking causes cancer.')
        DBSession.add(model)
        # replace the code to create a MyModel instance
        manager = Manager()
        password = os.environ.get('ADMIN_PASSWORD', u'admin')
        password = manager.encode(password)
        admin = User(username=u'admin', password=password)
        DBSession.add(admin)
