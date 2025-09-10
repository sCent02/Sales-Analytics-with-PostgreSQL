-- Load data into PostgreSQL from CSV files
-- Make sure to adjust the file paths based on your environment

-- 1. Customers
COPY customers(customer_id, name, email, country)
FROM '/absolute/path/to/data/customers.csv'
DELIMITER ',' CSV HEADER;

-- 2. Products
COPY products(product_id, product_name, category, price)
FROM '/absolute/path/to/data/products.csv'
DELIMITER ',' CSV HEADER;

-- 3. Orders
COPY orders(order_id, customer_id, product_id, order_date, quantity)
FROM '/absolute/path/to/data/orders.csv'
DELIMITER ',' CSV HEADER;