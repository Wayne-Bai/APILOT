import pandas as pd
import sqlite3

# Create a SQL connection to our SQLite database
conn = sqlite3.connect('database.db')

# Read the SQL query into a DataFrame
df = pd.read_sql_query("SELECT * from table_name", conn)

# Close the connection
conn.close()
