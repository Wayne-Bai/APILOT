# Import necessary libraries
import pandas as pd

# Create a sample DataFrame (instead of actual data, use your own data)
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'C': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Compute pairwise correlation
corr_matrix = df.corr(numeric_only=True)

# Display the correlation matrix
print(corr_matrix)
