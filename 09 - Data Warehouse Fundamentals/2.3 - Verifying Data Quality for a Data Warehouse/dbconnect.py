import os
import psycopg2
pgpassword = "<replace this with your postgres password>"
conn = None
try:
    conn = psycopg2.connect(
        user = "postgres",
        password = "postgres",
        host = "localhost",
        port = "5433",
        database = "billingDW")
except Exception as e:
    print("Error connecting to data warehouse")
    print(e)
else:
    print("Successfully connected to warehouse")
finally:
    if conn:
        conn.close()
        print("Connection closed")