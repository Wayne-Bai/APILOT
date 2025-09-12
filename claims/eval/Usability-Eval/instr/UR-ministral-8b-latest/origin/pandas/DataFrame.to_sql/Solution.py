import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c']
}

df = pd.DataFrame(data)

# Database connection parameters
db_username = 'your_username'
db_password = 'your_password'
db_host = 'your_host'
db_port = 'your_port'
db_name = 'your_database'

# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')  # You can change the driver as per your database type.

# Write DataFrame to SQL
df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)

print("DataFrame has been written to the SQL database successfully.")
