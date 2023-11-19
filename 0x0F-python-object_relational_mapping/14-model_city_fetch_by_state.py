#!/usr/bin/python3
"""
Shebang to creat a PY script
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(State, City).filter(City.state_id == State.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
