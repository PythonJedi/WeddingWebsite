from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine("sqlite:////tmp/WeddingWebsiteTest.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

OrmBase = declarative_base()
OrmBase.query = db_session.query_property()

def init_db():
    from WeddingWebsite.Rsvp import Invitation, Unclaimed, Provisional, Confirmed, Pending
    OrmBase.metadata.create_all(bind=engine)
