import pandas as pd
from sqlalchemy import create_engine

# Sample DataFrame
data = {
    'Name': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'Age': [28, 34, 23],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Create a connection to the SQL database
engine = create_engine('sqlite:///mydatabase.db')  # Example using SQLite

# Write records stored in DataFrame to SQL database
df.to_sql('people', con=engine, index=False, if_exists='replace')
