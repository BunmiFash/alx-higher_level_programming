#!/usr/bin/python3

"""
A script that lists all State objects that contains the letter 'a'
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

    Session = sessionmaker(engine)
    session = Session()

    for id, name in session.query(
            State.id, State.name).order_by(State.id).filter(
                    State.name.like('%a%')):
        print('{}: {}'.format(id, name))
