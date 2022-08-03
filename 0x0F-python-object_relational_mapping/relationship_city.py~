#!/usr/bin/python3
"""
Ignoring SQL and trusting the ORM magic
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City class inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement="auto", primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
