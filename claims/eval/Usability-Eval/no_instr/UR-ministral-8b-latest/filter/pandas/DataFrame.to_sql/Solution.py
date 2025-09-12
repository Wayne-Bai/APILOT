import pandas as pd
from sqlalchemy import create_engine

# Replace 'database_type' with your specific SQLAlchemy database type
engine = create_engine('database_type://username:password@host/dbname')

# Assuming your DataFrame is named df
df = pd.read_csv('file.csv')  # Or you can create a DataFrame manually

# Write the DataFrame to the SQL database
df.to_sql('table_name', con=engine, if_exists='replace', index=False)
