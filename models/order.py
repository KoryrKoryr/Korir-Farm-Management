# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Import the Base class and session from the database module
from database import Base, session

# Define a new class Order that inherits from Base
class Order(Base):
    # Define the table name
    __tablename__ = "orders"

    # Define columns for the Order table
    id = Column(Integer, primary_key=True)  # Unique identifier for each order
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)  # Foreign key to the Product table
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)  # Foreign key to the Customer table
    quantity = Column(Integer, nullable=False)  # Quantity of the ordered product

    # Define relationships with the Product and Customer classes
    product = relationship('Product')
    customer = relationship('Customer')