#!/usr/bin/python3

"""
A script that modifies a state name state table
in the database hbtn_0e_6_usa
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

    session.query(State).filter(State.id == 2).update(
            {State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
