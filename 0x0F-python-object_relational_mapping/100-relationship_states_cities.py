#!/usr/bin/python3

"""
A script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    san = City(name="San Franscisco")
    cali.cities.append(san)
    session.add(cali)

    session.commit()
    session.close()
