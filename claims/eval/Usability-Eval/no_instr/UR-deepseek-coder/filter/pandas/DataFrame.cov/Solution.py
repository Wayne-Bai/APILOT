import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, None, 5],
    'B': [10, None, 30, 40, 50],
    'C': [100, 200, None, 400, 500]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()

print(covariance_matrix)
