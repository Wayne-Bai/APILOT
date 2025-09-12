
import pandas as pd
from sqlalchemy import create_engine

# create a connection to the database
engine = create_engine('postgresql://user:password@host:port/dbname')

# read the data from the table into a DataFrame
data = pd.read_sql("SELECT * FROM mytable", engine)
