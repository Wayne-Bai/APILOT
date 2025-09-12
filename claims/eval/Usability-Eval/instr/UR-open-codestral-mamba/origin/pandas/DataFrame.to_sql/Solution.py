import pandas as pd
from sqlalchemy import create_engine

# create sqlalchemy engine
engine = create_engine('sqlite://', echo=False)

# Assuming df is the DataFrame you want to write to the database
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Write DataFrame to a SQL table named 'my_table'
df.to_sql('my_table', con=engine)

# Now you can retrieve your data with SQL queries
sql_query = "SELECT * FROM my_table;"
result = engine.execute(sql_query).fetchall()
print(result)
