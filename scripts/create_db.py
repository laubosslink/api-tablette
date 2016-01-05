from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class Info(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    content = Column(String(), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "Info(%r, %r)" % (self.title, self.content)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sql')
    Base.metadata.create_all(engine)
