import pandas as pd

# Sample data
data = {'Names': ['Alice', 'Bob', 'Charlie'], 'Ages': [25, 30, 35]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create an Index from one of the DataFrame's columns
index = df.set_index('Names').index

# Retrieve the array representation of the Index
index_array = index.to_numpy()

print(index_array)
