import pandas as pd

# Assuming you have a SQL query and a connection to the database
# Replace 'your_query' with your actual SQL query and 'your_connection' with your actual database connection
query = 'your_query'
connection = 'your_connection'

# Read SQL query into a DataFrame
df = pd.read_sql_query(query, connection)
