#!/usr/bin/python3

"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id)
    for a in state:
        if state.filter(State.name.like('%a%')):
            print("{}: {}".format(a.id, a.name))
