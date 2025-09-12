import pandas as pd

# Create a sample DataFrame for demonstration
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 3, 2]
}

df = pd.DataFrame(data)

# Compute the pairwise correlation of columns in the DataFrame
correlation_matrix = df.corr()

print(correlation_matrix)
