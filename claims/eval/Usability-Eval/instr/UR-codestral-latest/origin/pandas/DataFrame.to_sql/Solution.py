import pandas as pd
from sqlalchemy import create_engine

# Assuming you have a DataFrame `df` and your database details are as follows
database_username = 'your_username'
database_password = 'your_password'
database_ip = 'localhost'
database_name = 'your_database'
table_name = 'your_table'

# Create a connection to the database using SQLAlchemy
engine = create_engine(f'postgresql://{database_username}:{database_password}@{database_ip}/{database_name}')

# Write the dataframe to a sql database
df.to_sql(table_name, engine, if_exists='replace', index = False)
