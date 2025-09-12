import pandas as pd

# Assuming you have a MySQL database with a table called 'sample_table'
# Replace the below with your own connection details
connection = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database'
}

# Create a SQL query string
query = 'SELECT * FROM sample_table'

# Use pandas' read_sql() function to execute the query and load the data into a DataFrame
df = pd.read_sql(query, con=connection)

# Display the DataFrame
print(df)
