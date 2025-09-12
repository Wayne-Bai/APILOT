import pandas as pd
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('your_database.db')

# Define your SQL query
query = "SELECT * FROM your_table"

# Read the SQL query into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the DataFrame
print(df)
