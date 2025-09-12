import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Hide the entire index
print(df.to_string(index=False))

# Hide specific keys in the index (e.g., hide index key 1)
df_filtered = df.drop(index=1)
print(df_filtered)
