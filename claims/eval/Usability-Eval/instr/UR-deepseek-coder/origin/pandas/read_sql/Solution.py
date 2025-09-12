import pandas as pd
from sqlalchemy import create_engine

# Define your database connection string
db_connection_str = 'mysql+pymysql://username:password@host:port/dbname'

# Create an SQLAlchemy engine
engine = create_engine(db_connection_str)

# Read SQL query or table into a DataFrame
df = pd.read_sql('SELECT * FROM your_table_name', con=engine)

# Display the DataFrame
print(df)
