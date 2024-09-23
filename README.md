# Korir Farm Management CLI Application

This is a command line interface application for managing your farm products, orders and customers. It is a simple farm management system that allows farmers to manage their inventory, track sales and interact with customers streamlining the process of farm products management and sales process.

## Features

**Inventory management:**

- Add new farm products with stock and price.
- Display all farm products with stock and price
- Update farm products stock and price.
- Delete old farm products from inventory.

**Sales management:**

- Place new orders
- Display all orders
- Display orders by customer
- Calculate the total price of an order
- Cancel an order

**Customer management:**

- Add new customers
- Display all customers
- Delete existing customers

## Technologies Used

- **Python:** Main programming language for the application.
- **SQLAlchemy:** ORM (Object Relational Mapping) to interact with database.
- **Alembic:** For managing database migration.
- **Click:** For building command line interface.

## Setup and Installation

1. Clone the repository from GitHub.

   - `git clone https://github.com/KoryrKoryr/Korir-Farm-Management.git'
   - `cd Korir-Farm-Management`

2. Set up the virtual environment and install dependencies.
   The project uses `Pipenv` to manage the dependencies and the virtual environment. Install Pipenv if it's not already installed:

   - `pip install pipenv`

   Install the project dependencies:

   - `pipenv install`

3. Activate the virtual environment:

   - `pipenv shell`

## Database Setup

This project uses SQLite for the database. You need to set up the database by running Alembic migrations.

After setting up the project, you must apply migrations to set up the database schema. Do this by running the following command:

- `alembic upgrade head`

## Available CLI Commands

**General Commands:**

- `python cli.py`: Displays a welcome message and a list of available commands.

**Product Management Commands:**

- `python cli.py product-management.py`: Displays product management menu. Manage farm products including adding, updating, displaying and deleting products.

**Customer Management Commands:**

- `python cli.py customer-management.py`: Displays customer management menu. Manage customers including adding, displaying and deleting customers.

## **Order Management Commands:**

- `python cli.py order-management.py`: Displays order management menu. Manage orders including placing orders, displaying all orders, calculating order prices, displaying orders by customer and canceling orders.

## Usage

**Seed Data:**

- In the `seed_data.py` file, you can seed data to populate the tables. You can use the `python seed_data.py` command to seed data for products, customers and orders. Check the database to confirm whether the data has been seeded successfully.

- Expect the following output when `python seed_data.py` is executed:

```
Seeded 7 products.
Seeded 5 customers.
Seeded 5 orders.
```

**Run CLI:**

- Use the `python cli.py` command to run the CLI. This will display the following welcome message and a list of available commands:

```

*********************************
Welcome to Korir's Farm!
This is a simple farm management system.
Manage your farm products, orders and customers.
*********************************

Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  customer-management
  order-management
  product-management

```

- Use the `python cli.py COMMAND` command to run a specific command. For example:

  - `python cli.py product-management` to run the product management command. Expect the following output:

```
*********************************
Welcome to Korir's Farm!
This is a simple farm management system.
Manage your farm products, orders and customers.
*********************************


Product Management Menu:
1. Add a New Farm Product
2. Delete Existing Product
3. Display All Products
4. Update Product Stock
5. Update Product Price
6. Back to Main Menu
Enter your choice (1-6):
```

- `python cli.py order-management` to run the order management command.Expect the following output:

```
*********************************
Welcome to Korir's Farm!
This is a simple farm management system.
Manage your farm products, orders and customers.
*********************************


Order Management Menu:
1. Place New Order
2. Cancel Existing Order
3. Display All Orders
4. Display Orders by Customer
5. Calculate Price for an Order
6. Back to Main Menu
Enter your choice (1-6):
```

- `python cli.py customer-management` to run the customer management command. Expect the following output:

```
*********************************
Welcome to Korir's Farm!
This is a simple farm management system.
Manage your farm products, orders and customers.
*********************************


Customer Management Menu:
1. Add a New Customer
2. Delete Existing Customer
3. Display All Customers
4. Back to Main Menu
Enter your choice (1-4):
```
