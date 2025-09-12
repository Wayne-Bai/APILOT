# Importing pandas library
import pandas as pd
from sqlalchemy import create_engine

# Define your database connection string
# You can configure this string according to your database type (e.g., MySQL, PostgreSQL, SQLite, etc.)
DATABASE_URL = 'postgresql://username:password@host:port/db_name'

# Create engine object for your database connection
engine = create_engine(DATABASE_URL)

# SQL query string
SQL_QUERY = 'SELECT * FROM table_name'

# Use'read_sql_query' function from pandas library to execute SQL query and store in a DataFrame
df = pd.read_sql_query(SQL_QUERY, engine)

# Print DataFrame for verification
print(df)
