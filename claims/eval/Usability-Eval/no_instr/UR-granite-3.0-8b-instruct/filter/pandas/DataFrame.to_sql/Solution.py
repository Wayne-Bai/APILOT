import pandas as pd
import sqlite3

# Assuming df is your DataFrame and 'table_name' is the name of the table in the SQL database
conn = sqlite3.connect('database.db')
df.to_sql('table_name', conn, if_exists='replace', index=False)
conn.close()
