import click
from models.product import Product
from models.customer import Customer
from models.order import Order



@click.group()
def cli():
    pass

@click.command()
def welcome():
    click.echo("*********************************")
    click.echo("Welcome to Korir's Farm!")
    click.echo("This is a simple farm management system.")
    click.echo("Manage your farm products, orders and customers.")
    click.echo("*********************************\n")

    cli()

if __name__ == '__main__':
    welcome()