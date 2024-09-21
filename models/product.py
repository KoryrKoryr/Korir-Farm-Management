# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import the Base class from the database module
from database import Base, session

# Define a new class Product that inherits from Base
class Product(Base):
    # Define the table name
    __tablename__ = "products"

    # Define columns for the Product table
    id = Column(Integer, primary_key=True)  # Unique identifier for each product
    name = Column(String, nullable=False, unique=True)  # Name of the product
    stock = Column(Integer, default=0)  # Stock, defaults to 0 if not provided

    # Create a new product with the given name and class
    @classmethod
    def create(cls, name, stock):
        product = cls(name=name, stock=stock)
        session.add(product)
        session.commit()

    # Deletes a product with the given name and stock.
    @classmethod
    def delete(cls, name, stock):
        product = cls(name=name, stock=stock)
        session.delete(product)
        session.commit()    