
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Function to return the first n rows
def get_first_n_rows(df, n):
    return df.head(n)

# Call the function with n as the number of rows you want to return
n = 3
result = get_first_n_rows(df, n)
print(result)
