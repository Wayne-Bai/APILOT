import pandas as pd
from sqlalchemy import create_engine

# Assuming you have a DataFrame named df with columns ['name', 'age', 'city']

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///example.db')

# Write records to the database
df.to_sql('table_name', con=engine, if_exists='replace', index=False)
