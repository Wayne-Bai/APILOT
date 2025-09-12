import pandas as pd
import sqlalchemy

# Establish a connection to the database using SQLAlchemy
database_url = "sqlite:///example.db"  # Use the appropriate database URL
engine = sqlalchemy.create_engine(database_url)

# Perform a query and load the result into a DataFrame
query = "SELECT * FROM my_table"  # Replace 'my_table' with your actual table name
df = pd.read_sql(query, con=engine)

# Show the DataFrame
print(df)
