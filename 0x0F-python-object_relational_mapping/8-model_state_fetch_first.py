#!/usr/bin/python3

"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State.id, State.name).order_by(State.id).all()

    if len(all_states) > 0:
        first = all_states[0]
        print('{}: {}'.format(first[0], first[1]))
    else:
        print("Nothing")
