import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Define a function to apply to each column
def multiply_by_2(x):
    return x * 2

# Apply the function along the axis (0 for columns, 1 for rows)
result = df.apply(multiply_by_2, axis=0)

print(result)
