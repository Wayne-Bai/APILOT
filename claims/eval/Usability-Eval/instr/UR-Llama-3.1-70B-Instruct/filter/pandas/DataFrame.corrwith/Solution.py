import pandas as pd
import numpy as np

# Generate a random DataFrame
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 5), columns=list('ABCDE'))

# Compute pairwise correlation without using pandas corr API
def pairwise_correlation(df):
    corr_matrix = df.T.apply(lambda x: (x - x.mean()) / x.std()).dot(df.T.apply(lambda x: (x - x.mean()) / x.std()).T) / (len(x) - 1)
    return corr_matrix

# Apply the function to the DataFrame
correlation_matrix = pairwise_correlation(df)

print(correlation_matrix)

# Optionally, to get the correlation coefficients only for certain columns
corr_cols = ['A', 'B', 'C']
subset_corr_matrix = pairwise_correlation(df[corr_cols])
print(subset_corr_matrix)

# To only keep coefficients with an absolute value greater than 0.5
print(correlation_matrix[(abs(correlation_matrix) > 0.5) & (correlation_matrix!= 1.000000)])
