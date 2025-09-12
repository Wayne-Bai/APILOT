# Import the pandas library and assign it a shorter alias 'pd'
import pandas as pd

# Read the SQL query into a DataFrame
def read_sql_query(query, db_connection, name=None):
    """
    Read a SQL query into a pandas DataFrame.

    Parameters:
    query (str): The SQL query to be executed.
    db_connection: The database connection object.
    name (str, optional): The name to be given to the newly created DataFrame. Defaults to None.

    Returns:
    pd.DataFrame: The DataFrame containing the result of the SQL query.
    """
    try:
        # Use pandas.read_sql_query() to read the SQL query into a DataFrame
        df = pd.read_sql_query(query, db_connection, name=name)
        return df
    except Exception as e:
        # Handle any exceptions that may occur during the execution of the SQL query
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
# Assume we have a SQLite database and a database connection object
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Define a SQL query to be executed
query = "SELECT * FROM customers"

# Read the SQL query into a DataFrame
df = read_sql_query(query, conn)

# Display the resulting DataFrame
print(df)
