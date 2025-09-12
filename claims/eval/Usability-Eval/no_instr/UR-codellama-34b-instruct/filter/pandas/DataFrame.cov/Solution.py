import pandas as pd

# create sample data frame
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})

# compute pairwise covariance excluding NA/null values
cov = df.cov(min_periods=1)
print(cov)
