# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Define a function to apply to each element
def square(x):
    return x ** 2

# Apply the function to each element in the DataFrame
df_squared = df.applymap(square)

print("\nDataFrame with squared values:")
print(df_squared)
