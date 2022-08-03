#!/usr/bin/python3
"""
Ignoring SQL and trusting the ORM magic
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" instance """


class State(Base):
    """ class State inherits from Base """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement="auto", primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
