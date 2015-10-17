from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import StaticPool

# http://docs.sqlalchemy.org/en/rel_1_0/dialects/sqlite.html#using-a-memory-database-in-multiple-threads
engine = create_engine('sqlite://',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)
Session = sessionmaker(bind=engine)
Base = declarative_base()
