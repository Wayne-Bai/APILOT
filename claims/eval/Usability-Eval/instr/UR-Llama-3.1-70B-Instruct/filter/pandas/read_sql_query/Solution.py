# Importing necessary libraries
import pandas as pd
import sqlite3

# Function to read SQL query into a DataFrame
def read_sql_query_into_df(db_name, query):
    """
    Reads SQL query into a DataFrame.

    Args:
    db_name (str): Name of the database file.
    query (str): SQL query.

    Returns:
    pd.DataFrame: DataFrame containing the result of the query.
    """
    try:
        # Establish a connection to the database
        conn = sqlite3.connect(db_name)

        # Read the SQL query into a DataFrame
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        return df

    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        return None


# Usage
if __name__ == "__main__":
    # Specify the database name
    db_name = "example.db"

    # Specify the SQL query
    query = "SELECT * FROM example_table"

    # Read the SQL query into a DataFrame
    df = read_sql_query_into_df(db_name, query)

    # Print the DataFrame
    if df is not None:
        print(df)
