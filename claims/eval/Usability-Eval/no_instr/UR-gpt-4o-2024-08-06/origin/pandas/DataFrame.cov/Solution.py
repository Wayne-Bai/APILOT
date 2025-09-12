import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, None, 2, 1],
    'C': [2, 3, 4, None, 6]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()

print(covariance_matrix)
