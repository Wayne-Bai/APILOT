import pandas as pd

# Sample data for demonstration
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Compute pairwise correlation
corr_matrix = df.corr()

print(corr_matrix)
