# Sales-Analytics-with-PostgreSQL
This project demonstrates my SQL skills by designing a **PostgreSQL database** for a simple sales system and writing queries to extract business insights.   It includes **schema design, sample data, and analytical queries** for real-world reporting use cases.

## 📂 Project Structure
- `schema.sql` → Defines tables (customers, products, orders)
- `insert_data.sql` → Inserts sample data into the tables
- `queries.sql` → Collection of analytical SQL queries
- `data/` → CSVs with sample data for loading

---

## 🛠️ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/sCent02/Sales-Analytics-with-PostgreSQL
   cd Sales-Analytics-with-PostgreSQL
   ```

2. Create a PostgreSQL database:

```bash
python init_db.py
```

3. Run queries:
```bash
python run_queries.py
```

## 📊 Example Insights

- Top 5 customers by spend

```sql
Running query:
 -- 1. Find top 5 customers by total spend
SELECT c.name, SUM(p.price * o.quantity) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5
                 name total_spent
0   Kristin Schneider    10357.67
1        Philip Lopez     5452.55
2  Natasha Thomas DDS     4967.39
3        Raymond Hall     3786.37
4    Christine Jarvis     2311.81
```


- Monthly sales trends

```sql
 -- 2. Monthly sales trend
SELECT DATE_TRUNC('month', order_date) AS month, SUM(p.price * o.quantity) AS monthly_sales
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY month
ORDER BY month
                      month monthly_sales
0 2025-03-01 00:00:00+08:00       6748.46
1 2025-04-01 00:00:00+08:00       4831.00
2 2025-05-01 00:00:00+08:00       2289.53
3 2025-06-01 00:00:00+08:00       4992.69
4 2025-07-01 00:00:00+08:00       6534.64
5 2025-08-01 00:00:00+08:00       7188.69
6 2025-09-01 00:00:00+08:00        110.88
```
- Best-selling product categories

```sql
-- 3. Best-selling product category
SELECT p.category, SUM(o.quantity) AS total_units_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_units_sold DESC
      category  total_units_sold
0         Toys                24
1  Electronics                23
2    Groceries                19
3        Books                17
4     Clothing                15
```


🚀 Skills Demonstrated
- Relational database design (PostgreSQL)
- Data manipulation with SQL
- Business analytics queries (joins, aggregations, window functions)
- Documentation and reproducibility
