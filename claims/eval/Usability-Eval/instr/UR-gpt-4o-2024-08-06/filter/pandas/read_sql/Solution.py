import pandas as pd
import sqlalchemy

# Create an engine instance. Replace 'SQLite' with your database type and 
# provide the correct connection string for your database.
engine = sqlalchemy.create_engine('sqlite:///your_database.db')

# Replace 'your_table_name' with your actual table name or SQL query
query = 'SELECT * FROM your_table_name'  # You can also directly provide a SQL query here.

# Execute the query and load data into a DataFrame
df = pd.read_sql(query, con=engine)

# Display the first few rows of the dataframe
print(df.head())
