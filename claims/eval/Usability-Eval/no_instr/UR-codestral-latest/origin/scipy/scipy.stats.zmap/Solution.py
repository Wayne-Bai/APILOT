import numpy as np
from scipy import stats

# Assuming 'data' is your dataset
data = np.array([...])  # Replace ... with your data

# Calculate the z-scores
z_scores = stats.zscore(data)

print(z_scores)
