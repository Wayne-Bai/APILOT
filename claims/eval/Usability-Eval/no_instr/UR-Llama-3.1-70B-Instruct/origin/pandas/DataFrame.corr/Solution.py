import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, np.nan],
    'D': [2, 3, 4, np.nan, 6]
}
df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr(min_periods=1)

print(correlation_matrix)
