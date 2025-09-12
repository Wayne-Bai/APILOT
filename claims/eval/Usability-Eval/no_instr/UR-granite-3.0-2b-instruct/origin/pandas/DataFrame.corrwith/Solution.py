import pandas as pd

# Assuming df is your DataFrame and it has numerical columns
# Compute pairwise correlation
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)
