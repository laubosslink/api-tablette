from create_db import Info

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

alldata = session.query(Info).all()
for somedata in alldata:
    print somedata
