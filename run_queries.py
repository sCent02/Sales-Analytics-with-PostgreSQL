import psycopg2
import pandas as pd

# Database connection
conn = psycopg2.connect(
    dbname="salesdb",
    user="postgres",
    password="postgres",  # replace with your password
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Read all queries from queries.sql
with open("queries.sql", "r") as f:
    sql_commands = f.read().split(";")  # split multiple queries by ;

for query in sql_commands:
    query = query.strip()
    if query:  # skip empty lines
        print("\nRunning query:\n", query)
        cur.execute(query)

        try:
            rows = cur.fetchall()
            df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
            print(df)
        except psycopg2.ProgrammingError:
            # query has no result set (e.g. CREATE TABLE)
            conn.commit()

cur.close()
conn.close()