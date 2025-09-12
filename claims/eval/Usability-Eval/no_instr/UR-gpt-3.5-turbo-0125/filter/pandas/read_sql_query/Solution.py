
import pandas as pd

# Read SQL query into a DataFrame
sql_query = "SELECT * FROM your_table"
connection = "your_database_connection_string"
df = pd.read_sql(sql_query, connection)

# Display the DataFrame
print(df)
