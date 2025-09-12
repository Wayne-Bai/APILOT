import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, None],
    'B': [4, 5, None, 6],
    'C': [7, None, 9, 10]
}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr()

print(correlation_matrix)
