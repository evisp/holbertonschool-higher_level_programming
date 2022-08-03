#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects
 from the database hbtn_0e_14_usa:
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}", pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
