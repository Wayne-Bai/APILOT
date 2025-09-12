import pandas as pd

# Read the data into a pandas DataFrame
df = pd.read_csv('data.csv')

# Compute pairwise correlation
corr_matrix = df.corr()

# Print the correlation matrix
print(corr_matrix)
