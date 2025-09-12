
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Perform the reduction operation (e.g. sum of all elements in the DataFrame)
result = df.values.sum()

print(result)
