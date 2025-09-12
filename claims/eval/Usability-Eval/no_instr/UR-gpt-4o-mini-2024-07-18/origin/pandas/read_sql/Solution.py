import pandas as pd
import sqlite3  # Example for SQLite, you can modify for other databases

# Establish a connection to the database
connection = sqlite3.connect('your_database.db')  # Replace with your database file or connection string

# Read SQL query or database table into a DataFrame
df = pd.read_sql_query("SELECT * FROM your_table_name", connection)  # Replace with your SQL query

# Close the connection
connection.close()

# Display the DataFrame
print(df)
