
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, np.nan], 'B': [4, 5, 6, np.nan], 'C': [7, 8, 9, np.nan]}
df = pd.DataFrame(data)

# compute pairwise covariance of columns excluding NA/null values
cov_matrix = df.cov()

print(cov_matrix)
