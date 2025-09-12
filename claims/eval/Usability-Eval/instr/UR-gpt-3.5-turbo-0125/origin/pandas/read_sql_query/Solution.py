
import pandas as pd

# Define the connection to the database
import sqlite3
conn = sqlite3.connect('database.db')

# Write the SQL query
sql_query = "SELECT * FROM table_name"

# Read SQL query into a DataFrame
df = pd.read_sql_query(sql_query, conn)

# Close the connection
conn.close()
