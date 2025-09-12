import pandas as pd

# Read SQL query into a DataFrame
df = pd.read_sql_query('SELECT * FROM table_name', conn)

# Read database table into a DataFrame
df = pd.read_sql_table('table_name', conn)
