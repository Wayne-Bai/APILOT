import pandas as pd

# Connection details - modify these as per your database
host = 'your_host'
database = 'your_database'
user = 'your_user'
password = 'your_password'

# Establish connection
db_connection = f'mysql://{user}:{password}@{host}/{database}'

# Execute SQL query
query = 'your_sql_query'

# Read data into a pandas DataFrame
df = pd.read_sql(query, db_connection)
