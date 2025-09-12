# Importing the pandas library
import pandas as pd
import numpy as np

# Sample DataFrame with object columns
data = {
    'A': ['1', '2', '3'],
    'B': ['a', 'b', 'c'],
    'C': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'D': ['10.5', '20.8', '30.1']
}

df = pd.DataFrame(data)

# Displaying the initial dtypes
print("Initial DataFrame dtypes:")
print(df.dtypes)

# Inference of dtypes using the apply function to convert the columns
df_inferred = df.apply(pd.to_numeric, errors='ignore')

# Convert the 'C' column to datetime
df_inferred['C'] = pd.to_datetime(df['C'], errors='ignore')

# Displaying the inferred dtypes
print("\nInferred DataFrame dtypes:")
print(df_inferred.dtypes)
