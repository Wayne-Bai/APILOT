# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Tom', 'Nick', 'John', 'Mike', 'Lucy', 'Rita'],
    'Age': [20, 21, 19, 18, 22, 20],
}
df = pd.DataFrame(data)

# Function to return the last n rows
def last_n_rows(df, n):
    """
    Return the last n rows of a DataFrame.
    
    Parameters:
    df (DataFrame): DataFrame to get the last rows from.
    n (int): Number of rows to return.
    
    Returns:
    DataFrame: Last n rows of the DataFrame.
    """
    return df.tail(n)

# Example usage:
print("Original DataFrame:")
print(df)
print("\nReturn the last 3 rows:")
print(last_n_rows(df, 3))
