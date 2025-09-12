import pandas as pd
from sqlalchemy import create_engine

# Define your database connection string
db_connection_str = 'mysql+pymysql://username:password@host:port/dbname'

# Create an SQLAlchemy engine
engine = create_engine(db_connection_str)

# Read SQL query or table into a DataFrame
# Example: Reading a table
df = pd.read_sql_table('your_table_name', con=engine)

# Example: Reading a query
query = "SELECT * FROM your_table_name WHERE some_column = 'some_value'"
df = pd.read_sql_query(query, con=engine)
