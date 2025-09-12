import numpy as np
import scipy.stats as stats

def coefficient_of_variation(data):
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # use ddof=1 for sample standard deviation
    cv = std_dev / mean
    return cv

# Example usage
data = np.array([5.1, 5.3, 5.5, 5.2, 5.8, 6.2, 6.4, 6.3, 5.2, 5.0])
print(f"Coefficient of Variation: {coefficient_of_variation(data):.2f}")
