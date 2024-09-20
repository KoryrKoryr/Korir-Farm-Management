# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import the Base class from the database module
from database import Base

# Define a new class Product that inherits from Base
class Product(Base):
    # Define the table name
    __tablename__ = "products"

    # Define columns for the Product table
    id = Column(Integer, primary_key=True)  # Unique identifier for each product
    name = Column(String, nullable=False, unique=True)  # Name of the product, cannot be null and must be unique
    stock = Column(Integer, default=0)  # Stock quantity of the product, defaults to 0 if not provided