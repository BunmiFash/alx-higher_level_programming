#!/usr/bin/python3

"""
A script that prints all City objects from the database
"""

from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, id, city in session.query(
            State.name, City.id, City.name).filter(
                    State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(state, id, city))
