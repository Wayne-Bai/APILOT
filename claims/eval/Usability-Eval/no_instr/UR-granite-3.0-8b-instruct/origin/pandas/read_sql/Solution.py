import pandas as pd

# Assuming you have a SQL query or a database table named 'table_name'
# Replace 'username', 'password', 'host', and 'database' with your actual credentials

# For SQL query
query = "SELECT * FROM table_name"
df = pd.read_sql_query(query, connection_details)

# For database table
df = pd.read_sql_table('table_name', connection_details)
