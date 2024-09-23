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

- `python cli.py order-management` to run the order management command. Expect the following output:

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

### Usage Examples

Here is a demonstration of some of the features that can be used in the CLI.

1. Adding a new customer.

```
$ python cli.py customer-management
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
Enter your choice (1-4): 1
Enter customer name: James Jerry
Customer James Jerry created successfully!
```

2. Adding a new farm product.

```
$ python cli.py product-management
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
Enter your choice (1-6): 1
Enter product name: Mangoes
Enter initial stock: 200
Enter product price: 35.00
Product Mangoes created successfully with 200 units of stock costing Ksh.35.00 per unit!
```

3. Placing a new order.

```
$ python cli.py order-management
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
Enter your choice (1-6): 1
Enter customer ID: 1
Enter product ID: 1
Enter quantity: 105
Order placed successfully for product ID 1!
```

4. Calculating price for an order.

```
$ python cli.py order-management
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
Enter your choice (1-6): 5
Enter order ID to calculate price: 1
Total price for order ID 1 is Ksh.3675.00
```

5. Display Orders by Customer.

```
$ python cli.py order-management
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
Enter your choice (1-6): 4
Enter customer ID: 1
Order ID: 1, Product: Mangoes, Quantity: 105

```

6. Cancelling an order.

```
$ python cli.py order-management
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
Enter your choice (1-6): 2
Enter order ID to cancel: 1
Order with ID 1 cancelled successfully!
```

7. Deleting a customer.

```
$ python cli.py customer-management
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
Enter your choice (1-4): 2
Enter customer ID to delete: 1
Customer with ID 1 deleted successfully!
```

8. Deleting a farm product.

```
$ python cli.py product-management
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
Enter your choice (1-6): 2
Enter product ID to delete: 1
Product with ID 1 deleted successfully!
```

- Demonstrating displaying of farm products, orders and customers with the seed data.

9. Displaying all farm products.

```
$ python cli.py product-management
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
Enter your choice (1-6): 3

All Products:
ID: 1, Name: Beetroot, Stock: 100, Price: Ksh.50.00/unit of stock
ID: 2, Name: Strawberries, Stock: 300, Price: Ksh.5.00/unit of stock
ID: 3, Name: Avocados, Stock: 50, Price: Ksh.30.00/unit of stock
ID: 4, Name: Maize, Stock: 400, Price: Ksh.800.00/unit of stock
ID: 5, Name: Cucumber, Stock: 79, Price: Ksh.25.00/unit of stock
ID: 6, Name: Bell Peppers, Stock: 138, Price: Ksh.15.00/unit of stock
ID: 7, Name: Beans, Stock: 125, Price: Ksh.100.00/unit of stock
```

10. Displaying all customers.

```
$ python cli.py customer-management
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
Enter your choice (1-4): 3

All Customers:
ID: 1, Name: Cher Maeve
ID: 2, Name: Pipo Latta
ID: 3, Name: Lailah Chebet
ID: 4, Name: Ian Leonard
ID: 5, Name: Kiki Miki
```

11. Displaying all orders.

```
$ python cli.py order-management

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
Enter your choice (1-6): 3

All Orders:
ID: 1, Product ID: 1, Customer ID: 1, Quantity: 10
ID: 2, Product ID: 2, Customer ID: 3, Quantity: 5
ID: 3, Product ID: 3, Customer ID: 5, Quantity: 12
ID: 4, Product ID: 4, Customer ID: 4, Quantity: 25
ID: 5, Product ID: 5, Customer ID: 2, Quantity: 17
```

- Demonstrating updating of farm product's stock and price.

1.  Updating product stock.

```
$ python cli.py product-management
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
Enter your choice (1-6): 3

All Products:
ID: 1, Name: Beetroot, Stock: 100, Price: Ksh.50.00/unit of stock
ID: 2, Name: Strawberries, Stock: 300, Price: Ksh.10.00/unit of stock
ID: 3, Name: Avocados, Stock: 97, Price: Ksh.30.00/unit of stock
ID: 4, Name: Maize, Stock: 400, Price: Ksh.800.00/unit of stock
ID: 5, Name: Cucumber, Stock: 79, Price: Ksh.25.00/unit of stock
ID: 6, Name: Bell Peppers, Stock: 138, Price: Ksh.15.00/unit of stock
ID: 7, Name: Beans, Stock: 125, Price: Ksh.100.00/unit of stock

Product Management Menu:
1. Add a New Farm Product
2. Delete Existing Product
3. Display All Products
4. Update Product Stock
5. Update Product Price
6. Back to Main Menu
Enter your choice (1-6): 4
Enter product ID to update: 5
Enter quantity to add to stock: 11
Stock updated for product with ID 5!

Product Management Menu:
1. Add a New Farm Product
2. Delete Existing Product
3. Display All Products
4. Update Product Stock
5. Update Product Price
6. Back to Main Menu
Enter your choice (1-6): 3

All Products:
ID: 1, Name: Beetroot, Stock: 100, Price: Ksh.50.00/unit of stock
ID: 2, Name: Strawberries, Stock: 300, Price: Ksh.10.00/unit of stock
ID: 3, Name: Avocados, Stock: 97, Price: Ksh.30.00/unit of stock
ID: 4, Name: Maize, Stock: 400, Price: Ksh.800.00/unit of stock
ID: 5, Name: Cucumber, Stock: 90, Price: Ksh.25.00/unit of stock
ID: 6, Name: Bell Peppers, Stock: 138, Price: Ksh.15.00/unit of stock
ID: 7, Name: Beans, Stock: 125, Price: Ksh.100.00/unit of stock
```

2.  Updaating product price.

```
$ python cli.py product-management

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
Enter your choice (1-6): 3

All Products:
ID: 1, Name: Beetroot, Stock: 100, Price: Ksh.50.00/unit of stock
ID: 2, Name: Strawberries, Stock: 300, Price: Ksh.5.00/unit of stock
ID: 3, Name: Avocados, Stock: 97, Price: Ksh.30.00/unit of stock
ID: 4, Name: Maize, Stock: 400, Price: Ksh.800.00/unit of stock
ID: 5, Name: Cucumber, Stock: 79, Price: Ksh.25.00/unit of stock
ID: 6, Name: Bell Peppers, Stock: 138, Price: Ksh.15.00/unit of stock
ID: 7, Name: Beans, Stock: 125, Price: Ksh.100.00/unit of stock

Product Management Menu:
1. Add a New Farm Product
2. Delete Existing Product
3. Display All Products
4. Update Product Stock
5. Update Product Price
6. Back to Main Menu
Enter your choice (1-6): 5
Enter product ID to update: 2
Enter new price: 10.00
Price updated for product with ID 2!

Product Management Menu:
1. Add a New Farm Product
2. Delete Existing Product
3. Display All Products
4. Update Product Stock
5. Update Product Price
6. Back to Main Menu
Enter your choice (1-6): 3

All Products:
ID: 1, Name: Beetroot, Stock: 100, Price: Ksh.50.00/unit of stock
ID: 2, Name: Strawberries, Stock: 300, Price: Ksh.10.00/unit of stock
ID: 3, Name: Avocados, Stock: 97, Price: Ksh.30.00/unit of stock
ID: 4, Name: Maize, Stock: 400, Price: Ksh.800.00/unit of stock
ID: 5, Name: Cucumber, Stock: 79, Price: Ksh.25.00/unit of stock
ID: 6, Name: Bell Peppers, Stock: 138, Price: Ksh.15.00/unit of stock
ID: 7, Name: Beans, Stock: 125, Price: Ksh.100.00/unit of stock
```

## Database Migration

This project uses `Alembic` for database migration.

1. **Genetating a new migration**
   - If you make changes to the database models, for example adding a new table or column, generate a new migration:
     - `alembic revision --autogenerate -m "Describe migration"`
2. **Applying migration**
   - Apply all pending migrations to the database:
     - `alembic upgrade head`
3. **Rollback migration**
   - To roll back the latest migration:
     - `alembic downgrade -1`
4. **Migration issues**

   - If you encounter issues when applying migrations, you can rollback the last migration and retry:

   ```
   alembic downgrade -1
   alembic upgrade head

   ```
