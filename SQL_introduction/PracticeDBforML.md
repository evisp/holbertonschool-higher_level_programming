# E-Commerce Analytics SQL Training Project

## High-Level Description

This project is designed to provide hands-on experience with relational databases and SQL in the context of an e-commerce platform. You will create a database, define and populate tables, perform analytical queries, and export data for machine learning applications. By completing this project, you will gain practical skills in database design, data manipulation, and integration with ML workflows.

### Objective
Build a database for an e-commerce platform and analyze user behavior, sales, and product trends. Finally, export data for use in predictive analytics.

---

## Tasks

### Task 1: Set Up the Environment
1. Install MySQL Server 8.0 on Ubuntu 22.04.
2. Set up VS Code with the MySQL extension for query execution.
3. Verify the setup by connecting to the MySQL server and running a simple query to ensure the environment is properly configured.

### Task 2: Create the Database
1. Create a new database for the e-commerce platform.
2. Ensure the database is properly configured and accessible.

### Task 3: Define Tables
1. Define a `Users` table with the following fields:
   - Unique user identifier
   - Name
   - Email address (must be unique)
   - Registration date
2. Define a `Products` table with the following fields:
   - Unique product identifier
   - Product name
   - Price
   - Stock quantity
3. Define an `Orders` table with the following fields:
   - Unique order identifier
   - User identifier (linked to the `Users` table)
   - Order date
4. Define an `OrderDetails` table with the following fields:
   - Unique order detail identifier
   - Order identifier (linked to the `Orders` table)
   - Product identifier (linked to the `Products` table)
   - Quantity of the product ordered

### Task 4: Populate Tables
1. Populate the `Users` table with sample user data.
2. Populate the `Products` table with sample product data.
3. Populate the `Orders` table with sample order data.
4. Populate the `OrderDetails` table with sample line items for orders.

### Task 5: Basic Queries
1. Write a query to retrieve all users who registered within a specific time frame.
2. Write a query to retrieve all products that are low in stock.

### Task 6: Join Queries
1. Write a query to list all orders along with the user details who placed them.
2. Write a query to retrieve all order details, including the product name and price, for each order.

### Task 7: Advanced Analytical Queries
1. Write a query to find the top-selling products by summing up the quantities sold.
2. Write a query to identify the most active customers based on the total number of orders.
3. Write a query to calculate total revenue grouped by month.

### Task 8: Update and Delete Operations
1. Write a query to update stock quantities after an order is placed.
2. Write a query to delete all orders older than a specific date (e.g., cleanup operation).

### Task 9: Data Validation and Constraints
1. Add constraints to ensure email uniqueness in the `Users` table.
2. Add a check constraint to ensure that the product price is always greater than zero.
3. Add a foreign key constraint to ensure data integrity between `Orders` and `Users`.

### Task 10: Export Data to CSV
1. Export the contents of the `Orders` table to a CSV file.
2. Export aggregated monthly revenue data to a CSV file.
3. Ensure the exported files are correctly formatted and can be used for downstream analysis or integration with an ML pipeline.

