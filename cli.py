import click
from models.product import Product
from models.customer import Customer
from models.order import Order
from database import session
from helpers import validate_product_name, calculate_order_price

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    # Display welcome message
    click.echo("*********************************")
    click.echo("Welcome to Korir's Farm!")
    click.echo("This is a simple farm management system.")
    click.echo("Manage your farm products, orders and customers.")
    click.echo("*********************************\n")

    # Show help if no subcommand is passed
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

# Product Management Commands
@cli.command()
def product_management():
    while True:
        # Display product management menu
        click.echo("\nProduct Management Menu:")
        click.echo("1. Add a New Farm Product")
        click.echo("2. Delete Existing Product")
        click.echo("3. Display All Products")
        click.echo("4. Update Product Stock")
        click.echo("5. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-5)", type=int)

        if choice == 1:
            # Tuple used to store collected product details
            product_info = (
                click.prompt("Enter product name"),
                click.prompt("Enter initial stock", type=int),
                click.prompt("Enter product price", type=float)
            )
            # Validate that the product name is unique using the helper function
            try:
                validate_product_name(product_info[0])  # Validate product name
                # Create new product
                Product.create(*product_info)  # Unpack tuple directly
                click.echo(f"Product {product_info[0]} created successfully with {product_info[1]} units of stock costing Ksh.{product_info[2]:.2f} per unit!")
            except ValueError as e:
                click.echo(f"Error: {e}")

        elif choice == 2:
            # Delete existing product
            product_id = click.prompt("Enter product ID to delete", type=int)
            try:
                Product.delete(product_id)
                click.echo(f"Product with ID {product_id} deleted successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")

        elif choice == 3:
            # Display all products
            products = Product.get_all()  # This can be a list of product objects
            product_list = [(p.id, p.name, p.stock, p.price) for p in products]  # Convert to list of tuples
            click.echo("\nAll Products:")
            for product in product_list:
                click.echo(f"ID: {product[0]}, Name: {product[1]}, Stock: {product[2]}, Price: Ksh.{product[3]:.2f}/unit of stock")

        elif choice == 4:
            # Update product stock
            product_id = click.prompt("Enter product ID to update", type=int)
            quantity = click.prompt("Enter quantity to add to stock", type=int)
            # Dictionary used to store stock updates
            stock_update = {"product_id": product_id, "quantity": quantity}
            Product.update_stock(stock_update["product_id"], stock_update["quantity"])
            click.echo(f"Stock updated for product with ID {stock_update['product_id']}!")

        elif choice == 5:
            # Exit product management
            click.echo("Exiting Product Management...")
            break

# Customer Management Commands
@cli.command()
def customer_management():
    while True:
        # Display customer management menu
        click.echo("\nCustomer Management Menu:")
        click.echo("1. Add a New Customer")
        click.echo("2. Delete Existing Customer")
        click.echo("3. Display All Customers")
        click.echo("4. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-4)", type=int)

        if choice == 1:
            # Add a new customer
            name = click.prompt("Enter customer name")
            Customer.create(name)
            click.echo(f"Customer {name} created successfully!")

        elif choice == 2:
            # Delete an existing customer
            customer_id = click.prompt("Enter customer ID to delete", type=int)
            try:
                Customer.delete(customer_id)
                click.echo(f"Customer with ID {customer_id} deleted successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")

        elif choice == 3:
            # Display all customers
            customers = Customer.get_all()  # Assuming this returns a list of customer objects
            customer_list = [{"id": c.id, "name": c.name} for c in customers]  # Convert to list of dictionaries
            click.echo("\nAll Customers:")
            for customer in customer_list:
                click.echo(f"ID: {customer['id']}, Name: {customer['name']}")

        elif choice == 4:
            # Exit customer management
            click.echo("Exiting Customer Management...")
            break

# Order Management Commands
@cli.command()
def order_management():
    while True:
        # Display order management menu
        click.echo("\nOrder Management Menu:")
        click.echo("1. Place New Order")
        click.echo("2. Cancel Existing Order")
        click.echo("3. Display All Orders")
        click.echo("4. Display Orders by Customer")
        click.echo("5. Calculate Price for an Order")
        click.echo("6. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-5)", type=int)

        if choice == 1:
            # Place a new order. Dictionary to hold order details
            order_info = {
                "customer_id": click.prompt("Enter customer ID", type=int),
                "product_id": click.prompt("Enter product ID", type=int),
                "quantity": click.prompt("Enter quantity", type=int)
            }
            try:
                Order.create(order_info["product_id"], order_info["customer_id"], order_info["quantity"])
                click.echo(f"Order placed successfully for product ID {order_info['product_id']}!")
            except ValueError as e:
                click.echo(f"Error: {e}")

        elif choice == 2:
            # Cancel an existing order
            order_id = click.prompt("Enter order ID to cancel", type=int)
            try:
                Order.delete(order_id)
                click.echo(f"Order with ID {order_id} cancelled successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")

        elif choice == 3:
            # Display all orders
            orders = Order.get_all()  # List of order objects
            order_list = [(o.id, o.product_id, o.customer_id, o.quantity) for o in orders]  # Convert to list of tuples
            click.echo("\nAll Orders:")
            for order in order_list:
                click.echo(f"ID: {order[0]}, Product ID: {order[1]}, Customer ID: {order[2]}, Quantity: {order[3]}")

        elif choice == 4:
            # Display orders by customer
            customer_id = click.prompt("Enter customer ID", type=int)
            orders = Order.get_by_customer(customer_id)
            for order in orders:
                click.echo(f"Order ID: {order.id}, Product: {order.product.name}, Quantity: {order.quantity}")
        
        elif choice == 5:
            # Calculate price for an order
            order_id = click.prompt("Enter order ID to calculate price", type=int)
            try:
                total_price = calculate_order_price(order_id)  # Use the helper function
                click.echo(f"Total price for order ID {order_id} is Ksh.{total_price:.2f}")
            except ValueError as e:
                click.echo(f"Error: {e}")

        
        elif choice == 6:
            # Exit order management
            click.echo("Exiting Order Management...")
            break

# Main entry point
if __name__ == '__main__':
    cli()
