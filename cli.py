import click
from models.product import Product
from models.customer import Customer
from models.order import Order
from database import session



@click.group()
def cli():
    pass

#Welcome Message and then run CLI group
@click.command()
def welcome():
    click.echo("*********************************")
    click.echo("Welcome to Korir's Farm!")
    click.echo("This is a simple farm management system.")
    click.echo("Manage your farm products, orders and customers.")
    click.echo("*********************************\n")

    cli() # Invokes CLI group command

#Product Commands
@cli.command()
def product_management():
    while True:
        click.echo("\nProduct Management Menu:")
        click.echo("1. Add a New Farm Product")
        click.echo("2. Delete Existing Product")
        click.echo("3. Display All Products")
        click.echo("4. Update Product Stock")
        click.echo("5. Back to Main Menu")

        choice = click.prompt("Enter your choice (1-5): ", type=int)

        if choice == 1:
            name = click.prompt("Enter product name")
            stock = click.prompt("Enter initial stock", type=int)
            Product.create(name, stock)
            click.echo(f"Product {name} created successfully with {stock} units of stock!")
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
                click.echo(f"ID: {product.id}, Name: {product.name}, Stock: {product.stock}")
        elif choice == 4:
            product_id = click.prompt("Enter product ID to update:", type=int)
            quantity = click.prompt("Enter quantity to add to stock:", type=int)
            Product.update_stock(product_id, quantity)
            click.echo(f"Stock updated for product with ID {product_id}!")
        elif choice == 5:
            break

#Main entry point
if __name__ == '__main__':
    welcome()