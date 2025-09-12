import pandas as pd

# Assuming you have a connection object called "connection" to your database
# Replace "SELECT * FROM table_name" with your actual SQL query
df = pd.read_sql("SELECT * FROM table_name", connection)
