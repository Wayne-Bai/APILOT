import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3, 4, None],
    'B': [5, None, 7, 8, 9],
    'C': [10, 11, None, 13, 14]
}

df = pd.DataFrame(data)

# Compute the pairwise correlation, excluding NA/null values
correlation_matrix = df.corr()

print(correlation_matrix)
