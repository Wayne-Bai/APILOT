import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')

# Create a DataFrame with some example data
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': ['a', 'b', 'c', 'd', 'e']
})

# Write the DataFrame to a SQL table
df.to_sql('example_table', conn, index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()
