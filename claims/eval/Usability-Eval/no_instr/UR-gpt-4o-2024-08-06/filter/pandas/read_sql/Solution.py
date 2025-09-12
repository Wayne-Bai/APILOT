import pandas as pd
import sqlite3

# Establish a connection to the database
# Replace 'your_database.db' with your actual database file
connection = sqlite3.connect('your_database.db')

# Read SQL query or table into a DataFrame
# Replace 'your_sql_query' with your actual SQL query or 'your_table_name' with your actual table name
df = pd.read_sql_query('SELECT * FROM your_table_name', connection)

# Close the connection
connection.close()

# Display the DataFrame
print(df)
