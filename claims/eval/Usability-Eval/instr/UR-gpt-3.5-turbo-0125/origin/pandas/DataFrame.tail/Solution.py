
import pandas as pd

# Create a sample DataFrame for demonstration
data = {'A': [1, 2, 3, 4, 5],
        'B': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
df = pd.DataFrame(data)

# Function to return the last n rows
def return_last_n_rows(df, n):
    return df.tail(n)

# Specify the number of rows to return
n = 3

# Call the function to return the last n rows
result = return_last_n_rows(df, n)
print(result)
