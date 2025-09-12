import pandas as pd

# Assuming df is your DataFrame and it has columns A, B, C, ...
# Compute pairwise correlation of columns, excluding NA/null values
corr = df.corr(method='pearson', dropna=True)

# Print the correlation matrix
print(corr)
