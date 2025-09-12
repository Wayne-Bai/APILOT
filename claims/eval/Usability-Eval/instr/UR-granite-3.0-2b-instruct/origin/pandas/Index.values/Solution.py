import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Return an array representing the data in the Index
index_data = df.index.tolist()

print(index_data)
