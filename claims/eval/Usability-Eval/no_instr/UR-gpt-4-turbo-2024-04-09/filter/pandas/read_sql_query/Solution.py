import pandas as pd
from sqlalchemy import create_engine

# Establish a connection to the database
engine = create_engine('sqlite:///your_database.db')  # Update with your database URL

# Write your SQL query
query = "SELECT * FROM your_table"  # Update with your actual SQL query

# Read the data from SQL query into a DataFrame
df = pd.read_sql_query(query, engine)
