import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
 'name': ['Alice', 'Bob', 'Charlie'],
 'age': [25, 30, 35],
 'salary': [50000, 60000, 70000]
})

# Write the DataFrame to a SQL database
engine = pd.create_engine('sqlite:///:memory:')
df.to_sql('employees', engine, if_exists='replace')
