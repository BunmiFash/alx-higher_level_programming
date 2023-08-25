#!/usr/bin/python3

"""
A script that prints the state object with the
name passed as argument
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

    query = session.query(State.id).filter(State.name == '{}'.format(
        argv[4])).one_or_none()

    if query is not None:
        print(query[0])
    else:
        print("Not found")
