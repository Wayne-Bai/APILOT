import pandas as pd

# Assuming `df` is your DataFrame
correlation_matrix = df.corr(method='pearson', min_periods=1)
print(correlation_matrix)
