from models.product import Product
from models.order import Order
from database import session

# Helper function to validate the uniqueness of the product name
def validate_product_name(name):
    # Query the database to check if a product with the same name already exists
    existing_product = session.query(Product).filter_by(name=name).first()
    if existing_product:
        raise ValueError(f"Product with name '{name}' already exists!")

# Helper function to calculate the total price of an order
def calculate_order_price(order_id):
    """Calculate the total price for a given order."""
    # Fetch the order
    order = session.query(Order).get(order_id)
    
    if not order:
        raise ValueError(f"Order with ID '{order_id}' does not exist!")
    
    # Get the product details
    product = session.query(Product).get(order.product_id)
    
    if not product:
        raise ValueError(f"Product with ID '{order.product_id}' does not exist!")
    
    # Calculate total price: price of product * quantity ordered
    total_price = product.price * order.quantity
    return total_price

def update_product_price(product_id, new_price):
    # Get product from the database
    product = session.query(Product).filter_by(id=product_id).first()

    # Update the product's price
    if product:
        product.price = new_price
        session.commit()
    else:
        print(f"Product with ID {product_id} does not exist.")    