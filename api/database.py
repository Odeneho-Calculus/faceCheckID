# api/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URI = 'sqlite:///facecheck_bot.db'
engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))

def get_db_session():
    return Session()
