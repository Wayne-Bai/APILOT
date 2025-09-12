# Import necessary libraries
import pandas as pd
import sqlite3

# Create a DataFrame (example data)
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}
df = pd.DataFrame(data)

# Create a connection to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('example.db')

# Write DataFrame to a SQL database (sqlite3)
df.to_sql('people', conn, if_exists='replace', index=False)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
