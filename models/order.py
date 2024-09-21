# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Import the Base class and session from the database module
from database import Base, session

# Import the Product class from the models module
from models.product import Product

#Import the Customer class from the models module
from models.customer import Customer

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

    # Create new farm product order
    @classmethod
    def create(cls, product_id, customer_id, quantity):
        # Check if the customer exists in the database
        customer = session.query(Customer).get(customer_id)
        if not customer:
            raise ValueError(f"Customer with id {customer_id} not found!")        

        
        order = cls(product_id=product_id, customer_id=customer_id, quantity=quantity)
        session.add(order)

        # Update the stock of the ordered product
        product = session.query(Product).get(product_id)
        if product.stock < quantity:
            raise ValueError(f"Not enough stock available! Only {product.stock} available.")
        product.stock -= quantity

        session.commit()
        return order
    
    # Retrieve all orders from the database
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    # Retrieve orders for a specific customer from the database
    @classmethod
    def get_by_customer(cls, customer_id):
        return session.query(cls).filter_by(customer_id=customer_id).all()
    
    # Delete an order with given order_id from the database
    @classmethod
    def delete(cls, order_id):
        order = session.query(cls).get(order_id)
        if order:
            # Update the stock of the ordered product
            product = session.query(Product).get(order.product_id)
            if product:
                product.stock += order.quantity
            else:
                raise ValueError(f"Product with id {order.product_id} not found!")    
                    
            session.delete(order)
            session.commit()
        else:
            raise ValueError(f"Order with id {order_id} not found!")