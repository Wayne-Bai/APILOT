import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 2, np.nan, 4, 5]
})

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr().dropna()

print(correlation_matrix)
