import pandas as pd

# Replace 'my_connection' with your own database connection string
# Replace 'SELECT * FROM my_table' with your own SQL query
df = pd.read_sql('SELECT * FROM my_table', con='my_connection')

