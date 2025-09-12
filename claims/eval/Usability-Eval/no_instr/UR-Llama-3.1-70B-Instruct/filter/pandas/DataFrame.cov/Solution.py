# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame with random numeric data and NA/null values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, np.nan]
}
df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov()

# Print the covariance matrix
print(cov_matrix)
