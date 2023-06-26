#!/usr/bin/python3

"""
A script that adds the State
object “Louisiana” to the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3305/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    louis = State(name='Louisiana')
    session.add(louis)
    session.commit()

    for louis in session.query(State).filter(State.name == 'Louisiana'):
        print(louis.id)