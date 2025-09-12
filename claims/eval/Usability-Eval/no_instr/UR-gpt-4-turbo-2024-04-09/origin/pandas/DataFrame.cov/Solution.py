import pandas as pd

# Creating a sample dataframe
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, None, 8, 9],
    'C': [9, 8, 7, None, 5]
}

df = pd.DataFrame(data)

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()
print(covariance_matrix)
