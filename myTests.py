def sqlalchemy_test():
    config = 'development.ini'
    from pyramid.paster import get_appsettings
    settings = get_appsettings(config)
    from sqlalchemy import engine_from_config
    engine = engine_from_config(settings, 'sqlalchemy.')
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    from learning_journal.models import Entry
    Entry.by_id(session=session,entry_id=2)
    query = session.query(Entry.id, Entry.title, Entry.body, Entry.created, Entry.edited)
    for row in query:
        print row.id, type(row.id)
        print row.title, type(row.title)
        print row.body, type(row.body)
        print row.created, type(row.created)
        print row.edited, type(row.edited)

if __name__ == '__main__':
    sqlalchemy_test()


