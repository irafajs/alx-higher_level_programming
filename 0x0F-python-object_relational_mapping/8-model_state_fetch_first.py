#!/usr/bin/python3
"""
Shebang to create a python script
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    f_states = session.query(State).first()
    if (f_states):
        print("{}: {}".format(f_states.id, f_states.name))
    else:
        print("Nothing")
    session.close()
