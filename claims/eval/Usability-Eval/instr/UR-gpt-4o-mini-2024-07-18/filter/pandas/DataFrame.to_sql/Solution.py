
import pandas as pd
from sqlalchemy import create_engine

# Example DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Create a SQLAlchemy engine to connect to the database
engine = create_engine('sqlite:///my_database.db')  # Replace with your database connection string

# Write records to the SQL database
df.to_sql('my_table', con=engine, if_exists='replace', index=False)
