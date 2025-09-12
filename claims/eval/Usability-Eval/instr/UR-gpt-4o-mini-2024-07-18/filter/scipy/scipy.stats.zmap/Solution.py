import numpy as np
from scipy import stats

def relative_z_scores(data):
    z_scores = stats.zscore(data)
    relative_z = z_scores / np.max(np.abs(z_scores))
    return relative_z

# Example usage
data = [10, 12, 15, 14, 13, 18, 20]
relative_z = relative_z_scores(data)
print(relative_z)
