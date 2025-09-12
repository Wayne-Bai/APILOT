# Importing necessary libraries
import pandas as pd
import numpy as np

# Creating a DataFrame with random float values
df = pd.DataFrame(np.random.rand(5, 3), columns=list('ABC'))

# Introducing NA/null values
df.loc[0, 'A'] = np.nan
df.loc[2, 'B'] = np.nan
df.loc[4, 'C'] = np.nan

# Computing pairwise covariance of columns, excluding NA/null values
cov_df = df.cov()

# Printing the result
print(cov_df)
