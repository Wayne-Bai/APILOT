import pandas as pd

# Replace 'connection_string' with your actual SQL connection string
connection_string = 'your_connection_string_here'

# Replace 'your_sql_query' with your actual SQL query
sql_query = 'your_sql_query_here'

# Read SQL query into a DataFrame
df = pd.read_sql(sql_query, connection_string)
