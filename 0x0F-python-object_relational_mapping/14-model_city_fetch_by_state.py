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

    city_state = session.query(City, State).join(State).order_by(
            City.id)
    for city, state in city_state.all():
        print('{}: {} {}'.format(
            state.name, city.id, city.name))
