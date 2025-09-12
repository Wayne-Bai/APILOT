import pandas as pd
from sqlalchemy import create_engine

def read_sql_query(sql_query, engine):
    # Using SQLAlchemy to read the SQL query into a DataFrame
    df = pd.read_sql_query(sql_query, engine)
    return df

# Example usage:
# Create a SQLAlchemy engine (replace 'your_database_url' with your actual database URL)
engine = create_engine('your_database_url')

# Define your SQL query
sql_query = "SELECT * FROM your_table"

# Read the SQL query and store it in a DataFrame
df = read_sql_query(sql_query, engine)

# Display the DataFrame (optional)
print(df)
