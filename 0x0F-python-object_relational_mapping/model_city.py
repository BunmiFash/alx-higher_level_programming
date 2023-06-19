#!/usr/bin/python3

"""
Model - City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    City class
    """
    __tablename__ = "cities"
    id = Column(
            Integer, unique=True, nullable=False,
            primary_key=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer, ForeignKey(State.id), nullable=False)
