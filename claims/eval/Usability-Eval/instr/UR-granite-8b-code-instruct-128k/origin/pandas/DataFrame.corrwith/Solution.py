
import pandas as pd

# Assuming you have a DataFrame called 'df' with the following data:
#    A  B  C
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
# 3 10 11 12

# Compute pairwise correlation
corr_matrix = df.corr(method='pearson')

# Print the correlation matrix
print(corr_matrix)
