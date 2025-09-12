import pandas as pd
import sqlite3

# Establish a connection to the SQLite database
connection = sqlite3.connect('your_database.db')

# Define the SQL query
query = "SELECT * FROM your_table_name"

# Use the pandas read_sql function to execute the query and read data into a DataFrame
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Display the DataFrame
print(df)
