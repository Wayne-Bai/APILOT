import pandas as pd

# Assuming df is your DataFrame and it has columns 'A', 'B', 'C', etc.
df = pd.DataFrame({
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5]
})

# Compute pairwise correlation of columns, excluding NA/null values
corr = df.corr(method='pearson').iloc[1:, 1:]

print(corr)
