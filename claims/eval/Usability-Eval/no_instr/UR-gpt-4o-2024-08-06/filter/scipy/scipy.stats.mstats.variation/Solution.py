from scipy import stats
import numpy as np

def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    if mean == 0:
        return float('inf')
    return std_dev / mean

# Example usage:
data = [10, 12, 23, 23, 16, 23, 21, 16]
cv = coefficient_of_variation(data)
print("Coefficient of Variation:", cv)
