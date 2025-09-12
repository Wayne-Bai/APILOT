# Import the necessary libraries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Define the database connection parameters
username = 'your_username'
password = 'your_password'
host = 'your_host'
port = 'your_port'
database_name = 'your_database_name'

# Define the connection string
connection_string = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

try:
    # Create a database engine
    engine = create_engine(connection_string)

    # Create a sample DataFrame (replace with your actual DataFrame)
    data = {'Name': ['John', 'Anna', 'Peter'],
            'Age': [28, 24, 35],
            'Country': ['USA', 'UK', 'Australia']}
    df = pd.DataFrame(data)

    # Write the DataFrame to the SQL database (replace with your actual table name)
    df.to_sql('your_table_name', engine, if_exists='replace', index=False, method='multi')

    print("Data written to the SQL database successfully.")

except sqlalchemy.exc.OperationalError as e:
    print("Error connecting to the database: ", str(e))

except Exception as e:
    print("An error occurred: ", str(e))
