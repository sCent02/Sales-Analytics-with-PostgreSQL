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
   git clone https://github.com/YOUR_USERNAME/sql-sales-analytics.git
   cd sql-sales-analytics```

2. Create a PostgreSQL database:

```bash
createdb salesdb
psql -d salesdb -f schema.sql
psql -d salesdb -f insert_data.sql
```

3. Run queries:
```bash
psql -d salesdb -f queries.sql
```

## 📊 Example Insights

- Top 5 customers by spend
- Monthly sales trends
- Best-selling product categories

🚀 Skills Demonstrated
- Relational database design (PostgreSQL)
- Data manipulation with SQL
- Business analytics queries (joins, aggregations, window functions)
- Documentation and reproducibility
