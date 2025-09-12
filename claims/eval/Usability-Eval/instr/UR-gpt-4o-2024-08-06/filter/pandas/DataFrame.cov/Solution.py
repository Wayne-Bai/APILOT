import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, None, 1],
    'C': [10, 9, 8, 7, 6]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute the pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov()

# Display the covariance matrix
print(covariance_matrix)
