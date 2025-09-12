import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

# Desired index
new_index = [10, 11, 12, 13]

# Assign desired index to given axis
df.index = new_index

# Display the dataframe
print(df)
