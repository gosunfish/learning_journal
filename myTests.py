from ljshell import Session

def sqlalchemy_test():
    # config = 'development.ini'
    # from pyramid.paster import get_appsettings
    # settings = get_appsettings(config)
    # from sqlalchemy import engine_from_config
    # engine = engine_from_config(settings, 'sqlalchemy.')
    # from sqlalchemy.orm import sessionmaker
    # Session = sessionmaker(bind=engine)
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

#
# (learning-journal)carolyn.evans@d-108-179-161-174.dhcp4.washington.edu:~/Devel/learning-journal/learning_journal$ python
# Python 2.7.5 (default, Mar  9 2014, 22:15:05)
# [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from ljshell import Session
# >>> session = Session()
# >>> from learning_journal.models import Entry
# >>> e = Entry(title=u'Work, Damn you!!!', body=u'You makin me crazy')
# >>> e
# <learning_journal.models.Entry object at 0x10fc34a90>
# >>> session
# <sqlalchemy.orm.session.Session object at 0x10efb2210>
# >>> session.add(e)
# >>> session.commit()
# 2015-01-13 19:28:07,713 INFO  [sqlalchemy.engine.base.Engine][MainThread] SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
# 2015-01-13 19:28:07,714 INFO  [sqlalchemy.engine.base.Engine][MainThread] ()
# 2015-01-13 19:28:07,714 INFO  [sqlalchemy.engine.base.Engine][MainThread] SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
# 2015-01-13 19:28:07,714 INFO  [sqlalchemy.engine.base.Engine][MainThread] ()
# 2015-01-13 19:28:07,715 INFO  [sqlalchemy.engine.base.Engine][MainThread] BEGIN (implicit)
# 2015-01-13 19:28:07,716 INFO  [sqlalchemy.engine.base.Engine][MainThread] INSERT INTO entries (title, body, created, edited) VALUES (?, ?, ?, ?)
# 2015-01-13 19:28:07,716 INFO  [sqlalchemy.engine.base.Engine][MainThread] (u'Work, Damn you!!!', u'You makin me crazy', '2015-01-13 19:26:00.049310', '2015-01-13 19:26:00.049361')
# 2015-01-13 19:28:07,717 INFO  [sqlalchemy.engine.base.Engine][MainThread] COMMIT
# >>> https://github.com/UWPCE-PythonCert/training.python_web.git


# __call__ makes a class callable
# .pt means page template
# dev view(request) is a callable