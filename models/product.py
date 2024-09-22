# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

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
    price = Column(Float, nullable=False)  # Price of the product

    # Create a new farm product with the given name and stock
    @classmethod
    def create(cls, name, stock, price):
        product = cls(name=name, stock=stock, price=price)
        session.add(product)
        session.commit()
        return product

    # Deletes a farm product with the given product_id
    @classmethod
    def delete(cls, product_id):
        product = session.query(cls).get(product_id)
        if product:
            session.delete(product)
            session.commit()
        else:
            raise ValueError(f"Product with id {product_id} not found!")
    
    # Retrieve all farm products from database
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    # Retrieve a farm product by its id from database
    @classmethod
    def get_by_id(cls, product_id):
        return session.query(cls).get(product_id)
    
    # Updates the stock of a product with the given product_id
    @classmethod
    def update_stock(cls, product_id, new_stock):
        product = session.query(cls).get(product_id)
        if product:
            product.stock += new_stock
            session.commit()
        else:
            raise ValueError(f"Product with id {product_id} not found!")