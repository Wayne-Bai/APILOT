import pandas as pd
import sqlite3

# Assuming the database name is 'example.db' and the query string is 'SELECT * FROM your_table;'
connection = sqlite3.connect('example.db')
query = 'SELECT * FROM your_table;'

# Read SQL query into a DataFrame
df = pd.read_sql_query(query, connection)
