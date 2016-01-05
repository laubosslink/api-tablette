from create_db import Info,Comment,Post

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

print "INFOS:"

infos = session.query(Info).all()
for info in infos:
    print info

print "\nCOMMENTS:"

comments = session.query(Comment).all()
for comment in comments:
    print comment

print "\nPOSTS:"

posts = session.query(Post).all()
for post in posts:
    print post
    print post.comments
