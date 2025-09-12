import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 3, 7],
    'C': [None, 6, 8, 9]
}

df = pd.DataFrame(data)

# Fill NA/null values
df_filled = df.fillna(df.mean())

# Compute pairwise covariance excluding NA/null values
cov_matrix = df_filled.cov()

print(cov_matrix)
