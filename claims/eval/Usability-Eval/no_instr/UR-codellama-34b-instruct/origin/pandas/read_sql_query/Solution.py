
import pandas as pd

# Replace this with your own SQL connection string
connection_string = 'YOUR_CONNECTION_STRING'

# Connect to the database using the SQLAlchemy engine
engine = create_engine(connection_string)

# Execute the query and return the results as a pandas DataFrame
df = pd.read_sql('SELECT * FROM mytable', engine)
