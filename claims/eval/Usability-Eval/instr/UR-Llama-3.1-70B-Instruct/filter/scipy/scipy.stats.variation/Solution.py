# Import necessary libraries
import scipy.stats as stats
import numpy as np

# Define a function to compute the coefficient of variation
def compute_coefficient_of_variation(data):
    """
    Compute the coefficient of variation.

    Parameters:
    data (array-like): Input data.

    Returns:
    coefficient_of_variation (float): Coefficient of variation.
    """
    # Compute the mean
    mean = np.mean(data)
    
    # Compute the standard deviation
    std_dev = np.std(data, ddof=1)
    
    # Compute the coefficient of variation
    coefficient_of_variation = std_dev / mean
    
    return coefficient_of_variation

# Example usage:
data = [1, 2, 3, 4, 5]
coefficient_of_variation = compute_coefficient_of_variation(data)
print("Coefficient of Variation:", coefficient_of_variation)
