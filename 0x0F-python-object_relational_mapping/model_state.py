#!/usr/bin/python3

"""
A python file that contains the
class definition of a State and an instance
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint

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
