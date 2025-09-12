# Import necessary library
import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame(np.random.randint(0,100,size=(4, 4)), columns=list('ABCD'))

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Assign desired index to the rows
df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']

# Print the DataFrame after assigning new index to rows
print("\nDataFrame after assigning new index to rows:")
print(df)

# Assign desired index to the columns
df.columns = ['Col_A', 'Col_B', 'Col_C', 'Col_D']

# Print the DataFrame after assigning new index to columns
print("\nDataFrame after assigning new index to columns:")
print(df)
