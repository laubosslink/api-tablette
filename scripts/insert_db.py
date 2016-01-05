from create_db import Info

from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

m1 = Info("Monument de la beaute", "Existe depuis ... bla bla")

try:
    session.add(m1)
    session.commit()
except:
    session.rollback()
