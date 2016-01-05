from create_db import Info, Post, Comment

from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

i1 = Info("Monument de la beaute", "Existe depuis ... bla bla")

p1 = Post('Hello world', 'Sample post with hello world content')

c1 = Comment(p1, 'Just one answer for sample post')
c2 = Comment(p1, 'Just one answer for sample post')

try:
    session.add(i1)
    session.add(p1)
    session.add(c1)
    session.add(c2)
    session.commit()
except:
    session.rollback()
