#!/usr/bin/python3
"""
script that lists all State objects, and
corresponding City objects, contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(
            City).order_by(City.id).all()

    for state in query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
