import pandas as pd
from sqlalchemy import create_engine

# Create an engine to connect to SQLite database
engine = create_engine('sqlite:///mydatabase.db')

# Define the SQL query
query = "SELECT * FROM my_table"

# Use pandas read_sql_query function to fetch data into a DataFrame
df = pd.read_sql_query(query, engine)
