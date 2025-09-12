import pandas as pd

# Assuming df is your DataFrame
# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df.cov().loc[:, 'column1':'column2'].drop('column3', axis=0)
