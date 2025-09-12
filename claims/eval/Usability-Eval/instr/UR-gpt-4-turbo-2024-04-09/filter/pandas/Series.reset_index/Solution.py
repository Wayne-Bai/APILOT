import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Resetting index of DataFrame without using outdated APIs
new_df = df.reset_index(drop=True)
print(new_df)
