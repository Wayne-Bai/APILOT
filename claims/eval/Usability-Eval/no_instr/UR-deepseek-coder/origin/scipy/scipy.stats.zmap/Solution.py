import numpy as np
from scipy.stats import zscore

# Example data
data = np.array([10, 20, 30, 40, 50])

# Calculate z-scores
z_scores = zscore(data)

# Calculate relative z-scores
relative_z_scores = z_scores / np.sum(np.abs(z_scores))

print("Relative Z-scores:", relative_z_scores)
