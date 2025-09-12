import pandas as pd
import sqlite3  # Example using SQLite, modify for other databases

# Establish a connection to the database
connection = sqlite3.connect('your_database.db')

# Read SQL query or database table into a DataFrame using the newer pd.read_sql method
query = "SELECT * FROM your_table_name;"
df = pd.read_sql(query, connection)

# Close the connection
connection.close()

# Display the DataFrame
print(df)
