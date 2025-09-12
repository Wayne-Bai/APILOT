
import numpy as np
from scipy.stats import zscore

# Generate sample data
data = np.array([10, 20, 30, 40, 50])

# Calculate z-scores
z_scores = (data - np.mean(data)) / np.std(data)

print("Relative z-scores:", z_scores)
