# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = 'sqlite:///farm_inventory.db'

# Create an engine instance
engine = create_engine(DATABASE_URL)

# Create a sessionmaker bound to the engine
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a declarative base class
Base = declarative_base()

# Create a session instance
session = sessionLocal()

# Function to initialize the database schema
def init_db():
    Base.metadata.create_all(bind=engine)