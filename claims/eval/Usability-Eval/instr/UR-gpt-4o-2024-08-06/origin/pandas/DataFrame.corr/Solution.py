import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 2, 3, 2],
    'D': [10, 20, None, 40, 50]
}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr()

print(correlation_matrix)
