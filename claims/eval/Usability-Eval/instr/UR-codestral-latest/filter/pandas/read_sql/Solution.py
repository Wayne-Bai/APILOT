import pandas as pd
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('your_database.db')

# Use pandas to read sql query into a DataFrame
query = "SELECT column1, column2, column3 FROM your_table_name"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()
