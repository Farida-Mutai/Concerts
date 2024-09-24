from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Updated import

# Replace 'sqlite:///concerts.db' with your database URL if using another database
DATABASE_URL = 'sqlite:///concerts.db'

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# Create a base class for declarative class definitions
Base = declarative_base()

# Create all tables in the engine
Base.metadata.create_all(engine)
