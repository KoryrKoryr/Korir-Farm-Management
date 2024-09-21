# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import the Base class from the database module
from database import Base, session

# Define a new class Customer that inherits from Base
class Customer(Base):
    # Define the table name
    __tablename__ = "customers"

    # Define columns for the Customer table
    id = Column(Integer, primary_key=True)  # Unique identifier for each customer
    name = Column(String, nullable=False, unique=True)  # Name of the customer, cannot be null and must be unique

    # Create a new customer with the given name
    @classmethod
    def create(cls, name):
        customer = cls(name=name)
        session.add(customer)
        session.commit()
        return customer
    
    # Delete a customer with given customer_id
    @classmethod
    def delete(cls, customer_id):
        customer = session.query(cls).get(customer_id)
        if customer:
            session.delete(customer)
            session.commit()
        else:
            raise ValueError(f"Customer with id {customer_id} not found!")
        
    # Retrieve all customers from database
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    # Retrive all customers by their id from database
    @classmethod
    def get_by_id(cls, customer_id):
        return session.query(cls).get(customer_id)