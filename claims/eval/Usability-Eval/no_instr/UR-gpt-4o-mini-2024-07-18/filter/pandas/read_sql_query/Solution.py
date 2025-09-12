import pandas as pd
import sqlalchemy

# Create a connection to the database
# Replace the connection string with your actual database connection details
connection_string = 'dialect+driver://username:password@host:port/database'
engine = sqlalchemy.create_engine(connection_string)

# SQL query to be executed
query = "SELECT * FROM your_table_name"

# Read the SQL query into a DataFrame
df = pd.read_sql(query, engine)

# Close the connection
engine.dispose()

# Display the DataFrame
print(df)
