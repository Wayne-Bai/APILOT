import pandas as pd

# Read SQL query or database table into a DataFrame
df = pd.read_sql('SELECT * FROM your_table_name', con='your_database_connection')
