
import pandas as pd

# Create a sample dataframe
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [10, 9, 8, 7, 6]
}
df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov(min_periods=1)
print(cov_matrix)
