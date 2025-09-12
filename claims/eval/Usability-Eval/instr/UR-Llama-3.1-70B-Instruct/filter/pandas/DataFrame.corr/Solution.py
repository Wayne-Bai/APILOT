# Import the pandas library
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [6, np.nan, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
}
df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation = df.corr(min_periods=1)

# Print the correlation matrix
print(correlation)
