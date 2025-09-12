import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [2, 3, 4, 5],
    'C': [4, 5, 6, 7]
}
df = pd.DataFrame(data)

# Compute pairwise correlation
correlation_matrix = df.corr()

print(correlation_matrix)
