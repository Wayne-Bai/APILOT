import numpy as np
from scipy.stats import zscore

# Assume data is a numpy array with the dataset we want to analyze
data = np.array([10, 20, 30, 40, 50])

# Calculate the relative z-scores using scipy's zscore function
relative_z_scores = zscore(data)

print("Relative z-scores:", relative_z_scores)
