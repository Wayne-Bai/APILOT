import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to compute covariance for
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': [2, 3, 4, 5, 6]
})

# Drop NA/null values
df = df.dropna()

# Compute pairwise covariance
covariance_matrix = df.cov()

print(covariance_matrix)
