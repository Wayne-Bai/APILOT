import pandas as pd
import sqlite3

# Assuming df is your DataFrame and 'table_name' is the name of your table
df.to_sql('table_name', con=sqlite3.connect('your_database.db'), if_exists='replace', index=False)
