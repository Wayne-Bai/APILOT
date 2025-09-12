# Import the necessary library
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 5, 7, 11],
    'C': [3, 5, 7, 11, 13]
}
df = pd.DataFrame(data)

# Compute pairwise correlation
corr_matrix = df.corr(method='pearson')

# Print the correlation matrix
print(corr_matrix)
