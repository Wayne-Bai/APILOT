import pandas as pd
from sqlalchemy import create_engine

# Assuming 'dataframe' is our DataFrame and it is already defined

# Create a SQL engine to connect to the database
# Replace 'database_type', 'username', 'password', 'host', and 'database_name' with actual details
engine = create_engine('database_type://username:password@host/database_name')

# Write records stored in the DataFrame to a SQL database without using deprecated methods
dataframe.to_sql('table_name', con=engine, index=False, if_exists='append')
