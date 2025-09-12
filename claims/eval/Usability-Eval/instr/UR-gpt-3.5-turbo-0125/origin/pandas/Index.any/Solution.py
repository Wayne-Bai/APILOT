
import pandas as pd

# Create a sample dataframe
data = {'A': [0, 1, 0, 0],
        'B': [False, False, True, False]}

df = pd.DataFrame(data)

# Check if any element is Truthy in the dataframe
result = df.any().any()

print(result)
