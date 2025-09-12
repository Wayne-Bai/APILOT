import numpy as np
from scipy import stats

# Example data
data = [34, 25, 18, 27, 30]

# Calculate the relative z-scores
z_scores = (data - np.mean(data)) / np.std(data)

print("The relative z-scores are:", z_scores)
