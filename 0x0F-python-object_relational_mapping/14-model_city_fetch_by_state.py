#!/usr/bin/python3

"""
A script that prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
    session = Session()

    sess = session.query(City, State).join(State).all()

    for city, state in sess:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
