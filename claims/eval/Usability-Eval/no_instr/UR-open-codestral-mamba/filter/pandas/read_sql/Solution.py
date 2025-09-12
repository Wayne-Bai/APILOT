import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the database
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

# Define the SQL query
sql_query = "SELECT * FROM my_table"

# Read the SQL query into a DataFrame
df = pd.read_sql_query(sql_query, engine)
