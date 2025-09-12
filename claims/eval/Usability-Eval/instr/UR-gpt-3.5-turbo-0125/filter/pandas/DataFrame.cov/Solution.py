
import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 10, 10, 10, 10]}
df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov(min_periods=1)
print(covariance_matrix)
