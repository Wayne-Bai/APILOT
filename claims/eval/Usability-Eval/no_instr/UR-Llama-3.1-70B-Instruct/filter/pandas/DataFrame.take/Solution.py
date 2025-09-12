# Importing the pandas library
import pandas as pd
import numpy as np

# Creating a numpy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Converting numpy array to DataFrame
df = pd.DataFrame(array)

# Printing the DataFrame
print("Original DataFrame:")
print(df)

# Specifying the indices to return
indices = [0, 2]

# Using take() function to return elements at specified indices along an axis
print("\nElements at indices along axis=0 (rows):")
print(df.take(indices, axis=0))

print("\nElements at indices along axis=1 (columns):")
print(df.take(indices, axis=1))
