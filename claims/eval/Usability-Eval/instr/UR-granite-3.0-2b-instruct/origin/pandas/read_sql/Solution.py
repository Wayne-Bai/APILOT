import pandas as pd

# Replace 'your_database_name' and 'your_table_name' with your actual database and table names
# Also, replace 'your_connection_string' with your actual database connection string

# Establish a connection to the database
connection_string = 'your_connection_string'
df = pd.read_sql_query("SELECT * FROM your_table_name", connection_string)

# Print the DataFrame
print(df)
