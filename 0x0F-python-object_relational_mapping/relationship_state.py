#!/usr/bin/python3

"""
A python file that contains the
class definition of a State and an instance
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Class State that defines the table state
    """
    __tablename__ = 'states'
    id = Column(
            Integer, unique=True, nullable=False,
            primary_key=True, autoincrement=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
