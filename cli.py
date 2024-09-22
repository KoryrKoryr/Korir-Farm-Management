import click
from models.product import Product
from models.customer import Customer
from models.order import Order
from database import session



@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    # Display welcome message 
    click.echo("*********************************")
    click.echo("Welcome to Korir's Farm!")
    click.echo("This is a simple farm management system.")
    click.echo("Manage your farm products, orders and customers.")
    click.echo("*********************************\n")

    #Show help if no subcommand is passed
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

# Product Management Commands
@cli.command()
def product_management():
    while True:
        click.echo("\nProduct Management Menu:")
        click.echo("1. Add a New Farm Product")
        click.echo("2. Delete Existing Product")
        click.echo("3. Display All Products")
        click.echo("4. Update Product Stock")
        click.echo("5. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-5) ", type=int)

        if choice == 1:
            name = click.prompt("Enter product name")
            stock = click.prompt("Enter initial stock", type=int)
            price = click.prompt("Enter product price", type=float)
            Product.create(name, stock, price)
            click.echo(f"Product {name} created successfully with {stock} units of stock costing Ksh.{price: .2f} per unit!")
        elif choice == 2:
            product_id = click.prompt("Enter product ID to delete", type=int)
            try:
                Product.delete(product_id)
                click.echo(f"Product with ID {product_id} deleted successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")
        elif choice == 3:
            products = Product.get_all()
            click.echo("\nAll Products:")
            for product in products:
                click.echo(f"ID: {product.id}, Name: {product.name}, Stock: {product.stock}, Price: Ksh.{product.price:.2f}/unit of stock")
        elif choice == 4:
            product_id = click.prompt("Enter product ID to update", type=int)
            quantity = click.prompt("Enter quantity to add to stock", type=int)
            Product.update_stock(product_id, quantity)
            click.echo(f"Stock updated for product with ID {product_id}!")
        elif choice == 5:
            break

# Customer Management Commands
@cli.command()
def customer_management():
    while True:
        click.echo("\nCustomer Management Menu:")
        click.echo("1. Add a New Customer")
        click.echo("2. Delete Existing Customer")
        click.echo("3. Display All Customers")
        click.echo("4. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-4) ", type=int)

        if choice == 1:
            name = click.prompt("Enter customer name")
            Customer.create(name)
            click.echo(f"Customer {name} created successfully!")
        elif choice == 2:
            customer_id = click.prompt("Enter customer ID to delete", type=int)
            try:
                Customer.delete(customer_id)
                click.echo(f"Customer with ID {customer_id} deleted successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")
        elif choice == 3:
            customers = Customer.get_all()
            click.echo("\nAll Customers:")
            for customer in customers:
                click.echo(f"ID: {customer.id}, Name: {customer.name}")
        elif choice == 4:
            break
# Order Management Commands
@cli.command()
def order_management():
    while True:
        click.echo("\nOrder Management Menu:")
        click.echo("1. Place New Order")
        click.echo("2. Cancel Existing Order")
        click.echo("3. Display All Orders")
        click.echo("4. Display Orders by Customer")
        click.echo("5. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-5)", type=int)

        if choice == 1:
            customer_id = click.prompt("Enter customer ID", type=int)
            product_id = click.prompt("Enter product ID", type=int)
            quantity = click.prompt("Enter quantity", type=int)
            try:
                Order.create(product_id, customer_id, quantity)
                click.echo(f"Order placed successfully for product ID {product_id}!")
            except ValueError as e:
                click.echo(f"Error: {e}")
        elif choice == 2:
            order_id = click.prompt("Enter order ID to cancel", type=int)
            try:
                Order.delete(order_id)
                click.echo(f"Order with ID {order_id} cancelled successfully!")
            except ValueError as e:
                click.echo(f"Error: {e}")
        elif choice == 3:
            orders = Order.get_all()
            click.echo("\nAll Orders:")
            for order in orders:
                click.echo(f"ID: {order.id}, Product ID: {order.product_id}, Customer ID: {order.customer_id}, Quantity: {order.quantity}")
        elif choice == 4:
            customer_id = click.prompt("Enter customer ID", type=int)
            orders = Order.get_by_customer(customer_id)
            for order in orders:
                click.echo(f"order ID: {order.id}, Product: {order.product.name}, Quantity: {order.quantity}")
        elif choice == 5:
            break

#Main entry point
if __name__ == '__main__':
    cli()
    