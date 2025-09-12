
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, 5, 6],
        'C': [3, 4, 5, 6, 7]}

df = pd.DataFrame(data)

# Compute pairwise correlation
correlation_matrix = df.corr()
print(correlation_matrix)
