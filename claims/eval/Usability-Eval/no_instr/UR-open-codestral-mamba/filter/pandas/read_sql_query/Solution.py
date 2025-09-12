# The necessary library to be imported
import pandas as pd
from sqlalchemy import create_engine

# Note that depending on your setup and database, you might need to change the dialect+driver part (sqlite:///example.db)
engine = create_engine("sqlite:///example.db")

# The SQL query that we want to execute
sql_query = "SELECT * FROM some_table"

# Read SQL query into a DataFrame
df = pd.read_sql_query(sql_query, engine)
