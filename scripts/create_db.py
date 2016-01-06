from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, relationship, sessionmaker

import datetime

Base = declarative_base()

class Info(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    content = Column(String(), nullable=False)
    vote = Column(Integer, default=0)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "Info(%r, %r)" % (self.title, self.content)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    content = Column(String(), unique=False, nullable=False)
    vote = Column(Integer, default=0)
    date_creation = Column(DateTime, default=datetime.datetime.utcnow)

    post_id = Column(Integer, ForeignKey('post.id'))

    post = relation("Post", backref='comment', lazy=False)

    def __init__(self, post, content):
        self.content = content
        self.post = post

    def __repr__(self):
        return "Comment(post_id:%r, content:%r, date:%r)" % (self.post_id, self.content, self.date_creation)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=False, nullable=False)
    content = Column(String(), unique=False, nullable=False)
    #picture = Column(String())
    vote = Column(Integer, default=0)
    date_creation = Column(DateTime, default=datetime.datetime.utcnow)

    comments = relationship("Comment")

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def voteUp(self):
        self.vote += 1

    def __repr__(self):
        return "Post(id:%r, title:%r, content:%r, vote:%r, date:%r)" % (self.id, self.title, self.content, self.vote, self.date_creation)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sql')
    Base.metadata.create_all(engine)
