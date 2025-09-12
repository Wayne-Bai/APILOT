import numpy as np
from scipy.stats import zscore

# Example data
data = np.array([10, 20, 30, 40, 50])

# Calculate relative z-scores
relative_z_scores = zscore(data)

print("Relative Z-Scores:", relative_z_scores)
