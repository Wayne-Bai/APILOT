import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, None, 2, 1],
    'C': [2, 3, 4, 5, 6]
}

df = pd.DataFrame(data)

# Compute the pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr()

print(correlation_matrix)
