import pandas as pd
import numpy as np

# Create a DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'Score': [90, 85, 88]}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Given positional indices
index1 = 0
index2 = 1

# Function to return elements in the given positional indices along an axis
def get_elements_at_indices(df, index1, index2, axis=0):
    return df.loc[index1:index2, :]

# Call the function and print the result
print("\nElements in the given positional indices along axis 0:\n", get_elements_at_indices(df, index1, index2))

# For axis=1, you can modify the function to return rows
def get_elements_at_indices_axis1(df, index1, index2):
    return df.iloc[:, index1:index2+1]

# Call the function and print the result
print("\nElements in the given positional indices along axis 1:\n", get_elements_at_indices_axis1(df, index1, index2))
