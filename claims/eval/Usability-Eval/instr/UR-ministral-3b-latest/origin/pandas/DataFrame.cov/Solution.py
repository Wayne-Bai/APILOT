import pandas as pd

# Sample data
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, 3, None]
}

df = pd.DataFrame(data)

# Compute pairwise covariance, excluding NaN/null values
cov_matrix = df.loc[~df.isnull().any(axis=1)].cov()

print(cov_matrix)
