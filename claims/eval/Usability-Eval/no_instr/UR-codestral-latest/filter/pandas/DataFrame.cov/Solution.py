import pandas as pd

# Assuming that 'data.csv' is the name of your file
data = pd.read_csv('data.csv')

# Calculate the pairwise covariance of columns, excluding NA/null values
covariance_matrix = data.cov()

print(covariance_matrix)
