
import pandas as pd

# create a sample data frame with 4 columns
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})

# compute pairwise correlations between columns
correlations = df.corr()

# print the correlation matrix
print(correlations)
