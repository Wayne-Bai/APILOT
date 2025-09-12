import numpy as np

def coefficient_of_variation(data):
    """
    Calculate the coefficient of variation for a given dataset.
    
    Parameters:
    data (list or numpy array): The dataset for which to compute the coefficient of variation.
    
    Returns:
    float: The coefficient of variation.
    """
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)  # Use ddof=1 for sample standard deviation.
    
    if mean == 0:
        raise ValueError("Mean of the data is zero, coefficient of variation is undefined.")
    
    cv = std_dev / mean
    return cv

# Example usage:
data = [10, 12, 23, 23, 16, 23, 21, 16]
cv = coefficient_of_variation(data)
print(f"Coefficient of Variation: {cv}")
