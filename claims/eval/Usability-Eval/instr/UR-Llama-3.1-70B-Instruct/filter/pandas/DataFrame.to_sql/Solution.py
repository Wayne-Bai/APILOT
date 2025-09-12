import pandas as pd
import sqlite3

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
})

# Establish a connection to the SQL database
conn = sqlite3.connect('example.db')

# Write the DataFrame to a SQL table
df.to_sql('people', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
