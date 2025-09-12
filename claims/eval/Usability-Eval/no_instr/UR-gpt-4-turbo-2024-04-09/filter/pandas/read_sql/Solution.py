import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the database
engine = create_engine('sqlite:///your_database.db')  # Adjust the URL for your database

# Execute a SQL query and read the result into a DataFrame
query = "SELECT * FROM your_table_name;"
df = pd.read_sql_query(query, engine)

print(df)
