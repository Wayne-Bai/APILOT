import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [6, 7, 8, 9, 10]
})

# Define the positional indices
indices = [0, 2]

# Return elements at the given indices along axis=0 (rows)
result = df.iloc[indices]

print(result)
