from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, relationship, sessionmaker

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

    post_id = Column(Integer, ForeignKey('post.id'))

    post = relation("Post", backref='comment', lazy=False)

    def __init__(self, post, content):
        self.content = content
        self.post = post

    def __repr__(self):
        return "Comment(%r, %r)" % (self.post_id, self.content)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=False, nullable=False)
    content = Column(String(), unique=False, nullable=False)
    #picture = Column(String())
    vote = Column(Integer, default=0)

    comments = relationship("Comment")

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def voteUp(self):
        self.vote += 1

    def __repr__(self):
        return "Post(%r, %r, %r, %r)" % (self.id, self.title, self.content, self.vote)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sql')
    Base.metadata.create_all(engine)
