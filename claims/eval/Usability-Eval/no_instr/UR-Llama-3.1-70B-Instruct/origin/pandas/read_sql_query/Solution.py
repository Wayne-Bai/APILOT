# Import necessary libraries
import pandas as pd
from pandas import sql
import sqlite3

# Function to read SQL query into a DataFrame
def read_sql_query_to_dataframe(db_name, query):
    try:
        # Establish a connection to the database
        connection = sqlite3.connect(db_name)
        
        # Read the SQL query into a DataFrame
        df = pd.read_sql_query(query, connection)
        
        # Close the connection
        connection.close()
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the database name and SQL query
    database_name = 'example.db'
    query = 'SELECT * FROM example_table'
    
    # Call the function to read the SQL query into a DataFrame
    df = read_sql_query_to_dataframe(database_name, query)
    
    # Print the resulting DataFrame
    print(df)
