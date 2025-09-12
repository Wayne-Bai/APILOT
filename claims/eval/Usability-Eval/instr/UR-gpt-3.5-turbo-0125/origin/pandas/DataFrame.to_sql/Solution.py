
import pandas as pd

# Assuming 'data' is the DataFrame containing the records to be written to the SQL database
data = pd.DataFrame({'column1': [1, 2, 3],
                     'column2': ['A', 'B', 'C']})

# Assuming 'table_name' is the name of the table in the SQL database
table_name = 'example_table'

# Establishing connection to the SQL database
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')

# Writing records from the DataFrame to the SQL database
data.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
