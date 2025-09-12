import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, None, 3, 4, 5]
}
df = pd.DataFrame(data)

# Drop rows with any NA/null values
df_clean = df.dropna()

# Compute the pairwise correlation
correlation_matrix = df_clean.corr()

print(correlation_matrix)
