from models.product import Product
from models.customer import Customer
from models.order import Order
from database import session

# Seed data for products
def seed_products():
    products = [
        Product(name='Maize', stock=100, price=50.75),
        Product(name='Potatoes', stock=150, price=30.00),
        Product(name='Avocados', stock=50, price=25.50),
        Product(name='French Beans', stock=80, price=40.00),
    ]
    session.bulk_save_objects(products)
    session.commit()
    print(f"Seeded {len(products)} products.")

# Seed data for customers
def seed_customers():
    customers = [
        Customer(name='Jane Doe'),
        Customer(name='John Smith'),
        Customer(name='Peter Parker'),
    ]
    session.bulk_save_objects(customers)
    session.commit()
    print(f"Seeded {len(customers)} customers.")

# Seed data for orders
def seed_orders():
    # Assuming customers and products are already seeded
    orders = [
        Order(product_id=1, customer_id=1, quantity=10),
        Order(product_id=2, customer_id=2, quantity=5),
        Order(product_id=3, customer_id=3, quantity=12),
    ]
    session.bulk_save_objects(orders)
    session.commit()
    print(f"Seeded {len(orders)} orders.")

# Main function to seed all data
def seed_all():
    seed_products()
    seed_customers()
    seed_orders()

if __name__ == "__main__":
    seed_all()
