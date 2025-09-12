import pandas as pd

# Assuming you have a SQLite database named 'my_database.db'
# Replace 'my_table' with the name of your table
# Replace 'column1, column2, column3' with the names of your columns

df = pd.read_sql_query("SELECT * FROM my_table", pd.io.sqlite.SQLiteConnection('my_database.db'))

# If you want to select specific columns, you can modify the query like this:
# df = pd.read_sql_query("SELECT column1, column2, column3 FROM my_table", pd.io.sqlite.SQLiteConnection('my_database.db'))
