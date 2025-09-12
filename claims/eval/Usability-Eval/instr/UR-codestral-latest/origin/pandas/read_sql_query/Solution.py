# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine

# Create a SQLAlchemy engine
engine = create_engine('mysql+pymysql://username:password@localhost/dbname')

# Define the SQL query
query = "SELECT * FROM your_table"

# Use pandas to execute the query and store the results in a DataFrame
df = pd.read_sql(query, engine)
