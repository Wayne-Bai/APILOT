import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to compute covariance for
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': [2, 3, 4, 5, 6]
})

# Compute pairwise covariance of columns, excluding NA/null values
covariance_matrix = df[['column1', 'column2']].cov(skipna=True)

print(covariance_matrix)
