
import pandas as pd

# Connect to the database
connection = your_db_engine.connect()

# Execute the SQL query and fetch the results into pandas DataFrame
query = "SELECT * FROM your_table_name"
df = pd.read_sql(query, connection)

# Close the connection
connection.close()

# Display the DataFrame
print(df)
