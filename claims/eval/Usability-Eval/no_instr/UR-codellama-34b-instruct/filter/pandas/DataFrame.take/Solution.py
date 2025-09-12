import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Define the positional indices for the axis along which we want to extract elements
pos_indices = [0, 2]

# Extract elements at specified positions along the axis
result = df.iloc[pos_indices]

print(result)
