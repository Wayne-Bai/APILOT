
import numpy as np
from scipy import stats

# Generate example data
x = np.array([1, 2, 3, 4, 5])

# Calculate the mean and standard deviation of the data
mean = np.mean(x)
stddev = np.std(x)

# Calculate the relative z-scores
z_scores = (x - mean) / stddev
