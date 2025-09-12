import pandas as pd

# Create a sample DataFrame
data = {
    'A': [4, 5, 6, 2, 3],
    'B': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Function to get the index of the first occurrence of the minimum value
def first_minimum_index(df, axis=0):
    # Get the minimum value
    min_val = df.min(axis=axis)
    
    # Get the index of the first occurrence of the minimum value
    idx = df.loc[(df == min_val).iloc[0, :]].first_valid_index()
    
    return idx

# Get the index of the first occurrence of the minimum value
print(first_minimum_index(df))
