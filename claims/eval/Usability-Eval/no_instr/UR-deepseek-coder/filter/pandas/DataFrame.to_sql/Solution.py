import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'column1': [1, 2, 3],
    'column2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Database connection string
database_url = 'sqlite:///example.db'  # Example for SQLite, replace with your database URL

# Create a SQLAlchemy engine
engine = create_engine(database_url)

# Write the DataFrame to a SQL table
table_name = 'my_table'  # Replace with your desired table name
df.to_sql(table_name, con=engine, if_exists='replace', index=False)
