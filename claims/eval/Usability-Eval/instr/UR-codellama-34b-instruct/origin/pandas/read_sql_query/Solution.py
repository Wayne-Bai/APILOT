import pandas as pd
from pandas.io import sql

# Connect to the database using SQLAlchemy engine
engine = sqlalchemy.create_engine('postgresql://user:password@host/dbname')

# Execute the query and read the results into a DataFrame
df = pd.read_sql(sql='SELECT * FROM mytable', con=engine)
