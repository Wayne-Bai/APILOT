import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')

# Write your SQL query
query = "SELECT * FROM table_name"

# Read SQL query into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()
