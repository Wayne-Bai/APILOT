# Import pandas library
import pandas as pd

# Create a simple dataframe for demonstration purposes
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
    'Age': [28, 24, 35, 32, 40],
    'Country': ['USA', 'UK', 'Australia', 'Germany', 'USA']
}
df = pd.DataFrame(data)

# Function to return the last n rows
def return_last_n_rows(df, n):
    """
    Returns the last n rows of a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to get the last n rows from.
        n (int): The number of last rows to return.

    Returns:
        pd.DataFrame: The last n rows of the DataFrame.
    """
    return df.iloc[-n:]

# Example usage
n = 2  # Return the last 2 rows
last_n_rows = return_last_n_rows(df, n)
print(last_n_rows)
