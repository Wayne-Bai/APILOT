import pandas as pd
from sqlalchemy import create_engine

# Example DataFrame
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///example.db')

# Write records to a SQL database
df.to_sql('people', con=engine, if_exists='replace', index=False)
