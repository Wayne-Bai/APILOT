# Import pandas library
import pandas as pd

# Create a simple DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Function to prefix column labels
def prefix_labels(df, prefix):
    # Use dictionary comprehension to add prefix to column labels
    df.columns = [f'{prefix}_{col}' for col in df.columns]
    return df

# Prefix labels with string 'prefix_'
prefix_df = prefix_labels(df, 'prefix_')

print("Original DataFrame:")
print(df)
print("\nDataFrame after prefixing labels:")
print(prefix_df)
