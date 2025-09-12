
import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 1, 4, 5],
        'C': [5, 4, 3, 2, 1]}

df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.corr()

print(correlation_matrix)
