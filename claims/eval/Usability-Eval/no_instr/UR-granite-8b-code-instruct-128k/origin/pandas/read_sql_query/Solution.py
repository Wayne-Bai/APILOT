
import pandas as pd

# Establish a connection to the SQL database
engine = pd.read_sql_table(table_name, con='your_database_connection_string')

# Execute the SQL query and read the result into a DataFrame
df = pd.read_sql_query(sql_query, engine)
