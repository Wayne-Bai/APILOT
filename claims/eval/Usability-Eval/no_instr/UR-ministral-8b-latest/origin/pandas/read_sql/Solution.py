import pandas as pd
import sqlite3

# Connect to the database
# Using SQLite as an example, you can replace it with any other database using appropriate libraries.
conn = sqlite3.connect('example.db')

# Replace 'your_query' with your SQL query or table name
query = 'SELECT * FROM your_table_name'

# Read the query result or table into a DataFrame
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)
