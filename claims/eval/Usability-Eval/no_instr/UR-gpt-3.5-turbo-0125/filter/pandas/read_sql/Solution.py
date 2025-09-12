
import pandas as pd

# Read SQL query or database table into a DataFrame
query = "SELECT * FROM table_name"
connection = create_engine('sqlite:///database.db')
df = pd.read_sql_query(query, connection)
