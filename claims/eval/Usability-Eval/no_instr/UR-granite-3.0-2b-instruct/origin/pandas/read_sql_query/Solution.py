import pandas as pd

# Replace 'your_database_url' with your actual database URL
# Replace 'your_query' with your actual SQL query
query = 'your_query'
url = 'your_database_url'

# Read SQL query into a DataFrame
df = pd.read_sql_query(query, url)

# Print the DataFrame
print(df)
