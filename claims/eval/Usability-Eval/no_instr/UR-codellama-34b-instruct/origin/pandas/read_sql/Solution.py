
import pandas as pd

# Establish connection to database
conn = sqlite3.connect('mydatabase.db')

# Read SQL query into DataFrame
df = pd.read_sql_query("SELECT * FROM mytable", conn)

# Print the contents of the DataFrame
print(df)
