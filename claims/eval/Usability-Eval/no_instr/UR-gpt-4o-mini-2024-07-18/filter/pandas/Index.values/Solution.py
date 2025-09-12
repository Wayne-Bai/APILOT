import pandas as pd

# Example creation of a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Returning an array representing the data in the Index
index_array = df.index.to_numpy()
print(index_array)
