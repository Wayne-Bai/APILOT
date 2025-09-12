import numpy as np
from scipy import stats

def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # Using sample standard deviation
    cv = (std_dev / mean) * 100 if mean != 0 else np.nan  # Avoid division by zero
    return cv

# Example usage
data = [10, 12, 23, 23, 16, 23, 21, 16]
cv_result = coefficient_of_variation(data)
print("Coefficient of Variation:", cv_result)
