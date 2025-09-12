
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]}

df = pd.DataFrame(data)

# Specify the positional indices you want to retrieve along the columns axis
indices = [0, 2, 4]

# Retrieve the elements at the specified indices along the columns axis
result = df.iloc[:, indices]
print(result)
