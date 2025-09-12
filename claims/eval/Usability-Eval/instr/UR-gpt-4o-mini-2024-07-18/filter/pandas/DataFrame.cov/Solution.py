import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, None],
    'B': [4, 5, None, 7],
    'C': [None, 2, 3, 4]
}

df = pd.DataFrame(data)

# Compute the pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov(min_periods=1)

print(cov_matrix)
