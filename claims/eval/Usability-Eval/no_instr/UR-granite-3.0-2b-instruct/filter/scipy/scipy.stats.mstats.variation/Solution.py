import numpy as np
from scipy import stats

def compute_coefficient_of_variation(data):
    # Calculate mean
    mean = np.mean(data)

    # Calculate standard deviation
    std_dev = np.std(data, ddof=1)  # ddof=1 is used to calculate sample standard deviation

    # Calculate coefficient of variation
    cov = (std_dev / mean) if mean != 0 else np.inf  # Avoid division by zero

    return cov

# Example usage:
data = np.array([1, 2, 3, 4, 5])
cov = compute_coefficient_of_variation(data)
print(f"The coefficient of variation is: {cov}")
