import psycopg2
from clickhouse_driver import Client

# PostgreSQL connection
pg_conn = psycopg2.connect(
    dbname="test_db",
    user="admin",
    password="password",
    host="localhost",
    port=5432
)
pg_cursor = pg_conn.cursor()


# Fetch data from PostgreSQL
pg_cursor.execute("SELECT id, name, age FROM users;")
rows = pg_cursor.fetchall()
# ClickHouse connection
ch_client = Client(host='localhost', port=9000)
# Insert data into ClickHouse
for row in rows:
    ch_client.execute("INSERT INTO users (id, name, age) VALUES", [row])

print("Migration completed successfully!")

# Close connections
pg_cursor.close()
pg_conn.close()
