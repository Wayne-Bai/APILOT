import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [6, 5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6, 7]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()
print(covariance_matrix)
