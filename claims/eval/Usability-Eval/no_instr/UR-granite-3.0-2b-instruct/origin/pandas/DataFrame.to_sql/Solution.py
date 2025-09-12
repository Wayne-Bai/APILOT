import pandas as pd
import sqlalchemy

# Assuming you have a DataFrame df and a SQL database connection established

# Create an engine that knows how to talk to your database
engine = sqlalchemy.create_engine('your_database_url')

# Write the DataFrame to a SQL table
df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)
