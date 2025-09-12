import pandas as pd

# Assume we have a DataFrame df
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, None],
    'C': [1, 2, None, 4, None]
})

covariance = df.cov()
