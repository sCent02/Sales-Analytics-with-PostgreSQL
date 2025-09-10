import psycopg2

# Database credentials
DB_USER = "postgres"
DB_PASS = "postgres"   # 🔑 replace with your password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "salesdb"

# File paths
SCHEMA_FILE = "schema.sql"
INSERT_FILE = "insert_data.sql"

# Step 1: Connect to default 'postgres' DB and create salesdb if missing
conn = psycopg2.connect(
    dbname="postgres",
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True
cur = conn.cursor()

try:
    cur.execute(f"CREATE DATABASE {DB_NAME};")
    print(f"Database '{DB_NAME}' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{DB_NAME}' already exists.")

cur.close()
conn.close()

# Step 2: Connect to salesdb
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Step 3: Run schema.sql
with open(SCHEMA_FILE, "r") as f:
    cur.execute(f.read())
    conn.commit()
print("✅ Tables created from schema.sql")

# Step 4: Run insert_data.sql
with open(INSERT_FILE, "r") as f:
    cur.execute(f.read())
    conn.commit()
print("✅ Data inserted from insert_data.sql")

cur.close()
conn.close()
print("🎉 Database initialization complete.")