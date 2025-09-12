import pandas as pd
from sqlalchemy import create_engine

# create a data frame
df = pd.DataFrame({'col1': ['data1', 'data2', 'data3'], 'col2': ['data4', 'data5', 'data6']})

# create sql engine
engine = create_engine('sqlite:///mydatabase.db', echo=False)

# write data frame to SQL
sqlite_connection = engine.connect()
sqlalchemy_connection = df.to_sql("mytable", sqlite_connection)
sqlite_connection.close()
