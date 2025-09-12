# Import necessary libraries
import pandas as pd
import numpy as np

# Create DataFrame with some sample data
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'Score': [90, 85, 88]}
df = pd.DataFrame(data)

# Return an array representing the data in the Index
print(df.index.values)

# Output:
# [0 1 2]
