from models.product import Product
from models.customer import Customer
from models.order import Order
from database import session

# Seed data for products
def seed_products():
    products = [
        Product(name='Beetroot', stock=100, price=50.00),
        Product(name='Strawberries', stock=300, price=5.00),
        Product(name='Avocados', stock=50, price=30.00),
        Product(name='Maize', stock=400, price=800.00),
        Product(name='Cucumber', stock=79, price=25.00),
        Product(name='Bell Peppers', stock=138, price=15.00),
        Product(name='Beans', stock=125, price=100.00),
    ]
    session.bulk_save_objects(products)
    session.commit()
    print(f"Seeded {len(products)} products.")

# Seed data for customers
def seed_customers():
    customers = [
        Customer(name='Cher Maeve'),
        Customer(name='Pipo Latta'),
        Customer(name='Lailah Chebet'),
        Customer(name='Ian Leonard'),
        Customer(name='Kiki Miki'),
    ]
    session.bulk_save_objects(customers)
    session.commit()
    print(f"Seeded {len(customers)} customers.")

# Seed data for orders
def seed_orders():
    # Assuming customers and products are already seeded
    orders = [
        Order(product_id=1, customer_id=1, quantity=10),
        Order(product_id=2, customer_id=3, quantity=5),
        Order(product_id=3, customer_id=5, quantity=12),
        Order(product_id=4, customer_id=4, quantity=25),
        Order(product_id=5, customer_id=2, quantity=17),
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
