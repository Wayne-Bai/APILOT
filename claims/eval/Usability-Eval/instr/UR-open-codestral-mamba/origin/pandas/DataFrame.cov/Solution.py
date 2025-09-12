import pandas as pd

# Let's suppose we have a DataFrame df
df = pd.DataFrame({
  'A': [1, 2, None, 4, 5],
  'B': [6, 7, None, 9, 10],
  'C': [11, None, 13, 14, 15],
  'D': [16, 17, 18, 19, None],
  'E': [21, None, 23, 24, 25]
})

# Compute pairwise covariance of columns, excluding NA/null values.
cov = df.cov()

print(cov)
