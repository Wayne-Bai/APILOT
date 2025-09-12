import pandas as pd
import sqlite3

# Assuming df is your DataFrame and conn is your SQLite connection
df.to_sql('table_name', conn, if_exists='replace', index=False)
