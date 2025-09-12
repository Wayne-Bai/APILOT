import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 2, 3, 2],
    'C': [5, 3, 2, 1, 5]
}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns
correlation_matrix = df.corr()

print(correlation_matrix)
