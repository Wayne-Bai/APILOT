import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Boston', 'Chicago']
}

df = pd.DataFrame(data)

# Database connection string: (Format: 'dialect+driver://username:password@host:port/database')
# For example, an SQLite database can be specified as follows: 'sqlite:///test.db'
connection_string = 'sqlite:///example.db'

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Write the DataFrame to a SQL table
df.to_sql('users', con=engine, index=False, if_exists='replace')

# Close the engine connection if needed (especially within certain environments)
engine.dispose()
