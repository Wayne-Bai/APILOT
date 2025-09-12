import pandas as pd

# Replace 'your_connection_string' with your actual database connection string
# and 'your_query' with your SQL query

# Read SQL query into a DataFrame
df = pd.read_sql_query(your_query, your_connection_string)

# Print the DataFrame
print(df)
