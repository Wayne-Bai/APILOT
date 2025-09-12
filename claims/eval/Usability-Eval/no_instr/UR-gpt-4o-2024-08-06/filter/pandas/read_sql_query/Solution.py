import pandas as pd
import sqlite3

# Establish a connection to the SQLite database
connection = sqlite3.connect('your_database.db')

# Define your SQL query
query = "SELECT * FROM your_table"

# Read the SQL query into a DataFrame
df = pd.read_sql_query(query, connection)

# Close the database connection
connection.close()

# Display the DataFrame
print(df)
