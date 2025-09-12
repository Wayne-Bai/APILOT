import pandas as pd
import sqlite3  # Example: using sqlite3 for demonstration

# Establish a connection to the SQL database
conn = sqlite3.connect('your_database.db')

# Define your SQL query
sql_query = '''
SELECT * FROM your_table;
'''

# Read the SQL query into a DataFrame
dataframe = pd.read_sql_query(sql_query, conn)

# Display the DataFrame
print(dataframe)
