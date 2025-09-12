import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, None, 5],
    'B': [10, 20, None, 40, 50],
    'C': [100, None, 300, 400, 500]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()

print(covariance_matrix)
