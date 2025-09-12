import pandas as pd

# Create a sample DataFrame
data = {'A': [0, 0, 3, 1],
        'B': [False, False, False, False],
        'C': [None, None, None, None]}
df = pd.DataFrame(data)

# Check if any element in the DataFrame is Truthy
result = df.any().any()

print("Is there any Truthy value in the DataFrame?", result)
