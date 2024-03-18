#!/usr/bin/python3
"""this describes class state in database"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ A state class fectch within a database that is
    connected to MySQL table.
    Attr:
        id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='delete', backref="state")
