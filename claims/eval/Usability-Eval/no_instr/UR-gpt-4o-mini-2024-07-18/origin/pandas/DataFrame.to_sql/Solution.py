import pandas as pd
from sqlalchemy import create_engine

# Example DataFrame
data = {
    'column1': [1, 2, 3],
    'column2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Database connection
engine = create_engine('sqlite:///my_database.db')  # Example using SQLite; change connection string for other DBs

# Write the DataFrame to a SQL database
df.to_sql('my_table', con=engine, index=False, if_exists='replace')
