# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
    'Age': [25, 30, 35, 40, 45, 50],
}
df = pd.DataFrame(data)

# Function to return the last n rows
def get_last_n_rows(df, n):
    """Return the last n rows of a DataFrame"""
    return df.tail(n)

# Call the function with n = 3
print(get_last_n_rows(df, 3))
