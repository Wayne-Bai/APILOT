# Import the necessary libraries
import pandas as pd
from sqlalchemy import create_engine

# Define the SQL database connection parameters
host = 'your_host'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# Define the SQL table name
table_name = 'your_table_name'

# Define the engine
engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')

# Define the DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['NY', 'LA', 'Chicago', 'Boston']
}
df = pd.DataFrame(data)

# Write the DataFrame to the SQL database
df.to_sql(table_name, engine, if_exists='replace', index=False)
