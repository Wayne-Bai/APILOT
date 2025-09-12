import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 3, 8],
        'C': [2, 5, 7, 6]}
df = pd.DataFrame(data)

# Calculate pairwise covariance, excluding NA/null values
cov_matrix = df.corr()
cov_matrix

