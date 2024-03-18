#!/usr/bin/python3
"""this describes the class state with example of
Base = declarative_base() """


from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """ A city Class fectch within the database
    and connects to MySQL table.
    Attr:
        id, name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
