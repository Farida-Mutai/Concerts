from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///concerts.db')  # or your preferred DB URI
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# Create all tables in the engine
# Base.metadata.create_all(engine)
