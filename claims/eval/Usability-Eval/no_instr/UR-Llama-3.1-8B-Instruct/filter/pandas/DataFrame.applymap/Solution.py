# Import necessary libraries
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Define a function to apply element-wise to the DataFrame
def square(x):
    return x ** 2

# Apply the function to the DataFrame element-wise
# Method 1: Using the apply method
df_squared = df.applymap(square)
print("Element-wise squared values (Method 1):")
print(df_squared)

# Method 2: Using the numpy vectorize function
df_squared_vectorized = np.vectorize(square)(df)
print("\nElement-wise squared values (Method 2):")
print(df_squared_vectorized)

# Method 3: Using the pow (exponentiation) operator
df_squared_operators = df ** 2
print("\nElement-wise squared values (Method 3):")
print(df_squared_operators)
