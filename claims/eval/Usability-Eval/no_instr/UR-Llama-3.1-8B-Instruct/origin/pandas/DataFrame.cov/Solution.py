import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5, np.nan],
    'B': [6, np.nan, 8, 9, np.nan, np.nan],
    'C': [10, 11, np.nan, np.nan, 14, 15]
}
df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov(min_count=1)
print("Pairwise Covariance Matrix:")
print(cov_matrix)
