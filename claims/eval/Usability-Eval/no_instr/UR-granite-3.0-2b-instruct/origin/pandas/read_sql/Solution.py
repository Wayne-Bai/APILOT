import pandas as pd

# Read SQL query into a DataFrame
query = "SELECT * FROM your_table"
df = pd.read_sql_query(query, your_connection)

# Alternatively, read a table from a database into a DataFrame
# df = pd.read_sql_table('your_table', your_connection)

# Print the DataFrame
print(df)
