
import numpy as np

# Define a function to compute the coefficient of variation
def coefficient_of_variation(data):
    mean_val = np.mean(data)
    std_dev = np.std(data)
    
    if mean_val == 0:
        return 0  # returning 0 if mean is 0 to avoid division by zero
    else:
        coefficient_variation = std_dev / mean_val
        return coefficient_variation

# Example usage:
data = [10, 20, 30, 40, 50]
cv = coefficient_of_variation(data)
print("Coefficient of Variation:", cv)
