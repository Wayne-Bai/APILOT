import numpy as np
from scipy.stats import zscore

# Example data
data = np.array([10, 20, 30, 40, 50])

# Calculate z-scores
z_scores = zscore(data)

# Calculate relative z-scores
relative_z_scores = z_scores / np.linalg.norm(z_scores)

print("Relative z-scores:", relative_z_scores)
