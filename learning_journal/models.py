from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
    )

from zope.sqlalchemy import ZopeTransactionExtension

from cryptacular.bcrypt import BCRYPTPasswordManager as Manager

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
    value = sa.Column(sa.Integer)

sa.Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Entry(Base):
    __tablename__ = 'entries'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa. Column(sa.Unicode(255), unique=True, nullable=False)
    body = sa.Column(sa.UnicodeText, default=u'')
    created = sa.Column(sa.DateTime, default=datetime.utcnow)
    edited = sa.Column(sa.DateTime, default=datetime.utcnow)

    #The session parameter is used when this method is called from an interpreter vs. an HTTP call
    @classmethod
    def all(cls, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).order_by(sa.desc(cls.created)).all()

    #The session parameter is used when this method is called from an interpreter vs. an HTTP call
    @classmethod
    def by_id(cls, entry_id, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).get(entry_id)


        # or filter which is not as efficient, but can return zero or many rows.
        # session.query(cls).filter(id==entry_id)
        # get works for zero or one rows that match. otherwise barfs.

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.Unicode(255), nullable=False)
    password = sa.Column(sa.Unicode(255), nullable=False)
    created = sa.Column(sa.DateTime, default=datetime.utcnow)
    edited = sa.Column(sa.DateTime, default=datetime.utcnow)

    @classmethod
    def by_username(cls, username, session=None):
        if session is None:
            session = DBSession
        return session.query(cls).filter(cls.username==username).first()

    def verify_password(self, password):
        manager = Manager()
        return manager.check(self.password, password)

        # return manager.check('admin', 'admin')

sa.Index('user_index', User.username, unique=True, mysql_length=255)