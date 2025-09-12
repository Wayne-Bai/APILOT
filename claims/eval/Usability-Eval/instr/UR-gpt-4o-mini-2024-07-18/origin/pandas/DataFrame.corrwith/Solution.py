import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 7],
    'C': [10, 11, 12, 13, 14]
}

df = pd.DataFrame(data)

# Compute pairwise correlation
correlation_matrix = df.corr()

print(correlation_matrix)
