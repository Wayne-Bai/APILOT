import pandas as pd

# Sample DataFrame
data = {'index1': [1, 2, 3, 4],
        'index2': [10, 20, 30, 40]}

df = pd.DataFrame(data)

# Get the data in the Index
index_data = df.index  # Returns the index as an array

print(index_data)
