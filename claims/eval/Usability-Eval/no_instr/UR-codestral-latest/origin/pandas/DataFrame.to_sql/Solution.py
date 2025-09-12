import pandas as pd
from sqlalchemy import create_engine

# Let's assume you have a DataFrame df
# df = ...

# Create a connection to the database
# You should replace 'sqlite:///my_database.sqlite' with your own database URL
engine = create_engine('sqlite:///my_database.sqlite')

# Write the DataFrame to a SQL table called 'my_table'
df.to_sql('my_table', engine, if_exists='replace')
