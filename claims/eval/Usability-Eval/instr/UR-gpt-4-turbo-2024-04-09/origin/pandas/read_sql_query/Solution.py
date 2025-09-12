import pandas as pd
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("your_database_file.db")

# Write your SQL query
query = """
SELECT * FROM your_table_name;
"""

# Use the read_sql method to read the query into a DataFrame
df = pd.read_sql(query, con)

# Be sure to close the connection
con.close()

# Now you can work with the data in DataFrame 'df'
print(df.head())
