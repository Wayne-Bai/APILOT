
import pandas as pd

# Create a sample DataFrame
data = {'A': [0, 1, 2], 'B': [False, True, False]}
df = pd.DataFrame(data)

# Check if any element in the DataFrame is Truthy
result = df.any().any()

print(result)
