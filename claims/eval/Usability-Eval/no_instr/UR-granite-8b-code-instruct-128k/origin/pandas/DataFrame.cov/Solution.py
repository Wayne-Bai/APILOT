import pandas as pd

# Assuming df is your DataFrame
cov_matrix = df.cov(method='pearson', min_periods=1)
print(cov_matrix)