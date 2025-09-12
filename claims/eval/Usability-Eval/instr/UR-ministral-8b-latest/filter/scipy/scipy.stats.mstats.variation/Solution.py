import numpy as np
from scipy import stats

def coefficient_of_variation(data):
    # Calculate the mean of the data
    mean = np.mean(data)
    # Calculate variance of the data
    variance = np.var(data)
    # Calculate the standard deviation
    standard_deviation = np.sqrt(variance)
    # Compute the coefficient of variation
    cv = standard_deviation / mean
    return cv

# Example usage
data = [1, 2, 3, 4, 5]
cv = coefficient_of_variation(data)
print(f"Coefficient of variation: {cv}")
