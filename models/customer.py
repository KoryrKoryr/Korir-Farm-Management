# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import the Base class from the database module
from database import Base

# Define a new class Customer that inherits from Base
class Customer(Base):
    # Define the table name
    __tablename__ = "customers"

    # Define columns for the Customer table
    id = Column(Integer, primary_key=True)  # Unique identifier for each customer
    name = Column(String, nullable=False, unique=True)  # Name of the customer, cannot be null and must be unique