
import numpy as np
from scipy import stats

# Define sample data
data = np.array([10, 15, 20, 25, 30])

# Calculate z-scores
z_scores = stats.zscore(data)

# Output the z-scores
print("Z-scores:", z_scores)
