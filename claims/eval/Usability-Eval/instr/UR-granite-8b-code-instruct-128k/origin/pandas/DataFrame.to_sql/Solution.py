
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
 'Age': [25, 30, 35],
 'Gender': ['Female', 'Male', 'Male']})

# Write the DataFrame to a SQL database
engine = pd.create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine, if_exists='replace', index=False)

