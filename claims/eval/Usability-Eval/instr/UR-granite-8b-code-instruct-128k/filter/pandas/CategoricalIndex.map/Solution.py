import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Define a mapping dictionary
mapping = {'A': lambda x: x * 10, 'B': lambda x: x + 10, 'C': lambda x: x - 5}

# Map the values using the mapping dictionary
df_mapped = df.apply(mapping)

print(df_mapped)
