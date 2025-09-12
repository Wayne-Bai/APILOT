# Importing necessary libraries
import pandas as pd

# Creating a DataFrame with some data
data = {
    'A': [1, 2, 3, None, 5],
    'B': [4, 5, 6, 7, 8],
    'C': [9, 10, 11, 12, None]
}
df = pd.DataFrame(data)

# Computing pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov(na=True, drop=False)

print(cov_matrix)
