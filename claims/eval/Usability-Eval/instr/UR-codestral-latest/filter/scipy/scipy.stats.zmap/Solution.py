import numpy as np
from scipy import stats

def calculate_z_scores(data):
    z_scores = stats.zscore(data)
    return z_scores

# Example usage:
data = np.array([1, 2, 3, 4, 5])
print(calculate_z_scores(data))
