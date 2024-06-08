# api/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()

class SearchResult(Base):
    __tablename__ = 'search_results'
    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable=False)
    result_url = Column(String, nullable=False)

Base.metadata.create_all(engine)
