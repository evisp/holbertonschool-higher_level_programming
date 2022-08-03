#!/usr/bin/python3
"""
Ignoring SQL and trusting the ORM magic
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" instance """


class City(Base):
    """ class City inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement="auto", primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
