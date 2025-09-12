import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 2, 3, 2]
}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns
correlation_matrix = df.corr()

print(correlation_matrix)
