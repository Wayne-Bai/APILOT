import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Database connection string
db_connection_str = 'sqlite:///example.db'  # Example for SQLite, replace with your DB connection string

# Create a SQLAlchemy engine
engine = create_engine(db_connection_str)

# Write the DataFrame to a SQL table
df.to_sql('my_table', con=engine, if_exists='replace', index=False)
