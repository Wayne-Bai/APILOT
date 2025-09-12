import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, None],
    'B': [4, None, 6, 7],
    'C': [None, 1, 2, 3]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
cov_matrix = df.cov()

print(cov_matrix)
