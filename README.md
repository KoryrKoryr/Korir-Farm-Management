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
