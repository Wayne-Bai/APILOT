import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3, 4, 5, None, 7],
    'B': [7, None, 5, 4, 3, 2, 1],
    'C': [None, 2, 3, 4, 5, 6, 7]
}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr(method='pearson', min_periods=1)
print(correlation_matrix)
