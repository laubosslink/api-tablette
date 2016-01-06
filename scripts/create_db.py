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

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return "Info(id:%r, title:%r, content:%r)" % (self.id, self.title, self.content)

class Drawing(Base):
    __tablename__ = 'drawing'

    id = Column(Integer, primary_key=True)
    filename = Column(String(255), unique=True, nullable=False)
    date_creation = Column(DateTime, default=datetime.datetime.utcnow)
    date_modification = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "Drawing(id:%r, filename:%r, date_creation:%r, date_modification:%r)" % (self.id, self.filename, self.date_creation, self.date_modification)

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sql')
    Base.metadata.create_all(engine)
