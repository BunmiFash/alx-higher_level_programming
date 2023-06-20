#!/usr/bin/python3

"""
A script that lists all State objects,
and corresponding City objects, contained
in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    for col in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(
            col.id, col.name, col.state.name))
