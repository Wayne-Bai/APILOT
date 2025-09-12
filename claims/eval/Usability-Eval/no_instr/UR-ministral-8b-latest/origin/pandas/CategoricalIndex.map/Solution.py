import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40], 'C': ['a', 'b', 'c', 'd']}

# Creating a DataFrame
df = pd.DataFrame(data)

# Mapping function definition
def map_values(x):
    return x * 2  # Example function to double the values

# Quotation results to apply the function to all columns
mapped_df = df.applymap(map_values)

print(mapped_df)
