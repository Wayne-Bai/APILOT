
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Write records to a SQL database
database_path = 'sqlite:///data.db'
table_name = 'employee'

engine = create_engine(database_path)
df.to_sql(table_name, engine, if_exists='replace', index=False)
