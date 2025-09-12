# Import necessary libraries
import pandas as pd
import sqlite3  # Use your respective database driver (e.g., psycopg2 for PostgreSQL, mysql-connector-python for MySQL)

# Define a function to read SQL query or database table into a DataFrame
def read_sql_query_to_df(conn, query):
    """
    Reads SQL query or database table into a pandas DataFrame.

    Parameters:
    conn (database connection object): Connection to the database.
    query (str): SQL query to read from the database.

    Returns:
    pd.DataFrame: DataFrame containing the data from the SQL query.
    """
    try:
        # Use pandas read_sql_query function with a database connection
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a connection to the SQLite database (replace with your database)
    conn = sqlite3.connect('example.db')

    # Define an SQL query (replace with your query)
    query = "SELECT * FROM example_table"

    # Read the SQL query into a DataFrame
    df = read_sql_query_to_df(conn, query)

    # Print the resulting DataFrame
    if df is not None:
        print(df)

    # Close the database connection
    conn.close()
