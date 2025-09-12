import pandas as pd

# Example Data
data = {'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Perform a reduction operation, such as summing all values in the 'value' column
result = df['value'].sum()

print("Sum of all values:", result)
