# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Define a function to apply element-wise
def square(x):
    return x ** 2

# Apply the function element-wise to a specified column
df['A_squared'] = df['A'].apply(square)

# Apply the function element-wise to multiple specified columns
df['B_squared'] = df['B'].apply(square)
df['C_squared'] = df['C'].apply(square)

# Alternatively, you can use vectorized operations for better performance
df['A_squared_vectorized'] = df['A'] ** 2

print(df)
