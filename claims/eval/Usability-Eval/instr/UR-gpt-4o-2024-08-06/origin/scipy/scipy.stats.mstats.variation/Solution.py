import numpy as np

def coefficient_of_variation(data):
    """
    Compute the coefficient of variation (CV) for a given dataset.

    Parameters:
    data (list or np.array): A list or numpy array containing numerical data.

    Returns:
    float: The coefficient of variation of the dataset.
    """
    mean = np.mean(data)
    std_dev = np.std(data, ddof=0)  # Using population standard deviation

    if mean == 0:
        raise ValueError("Mean of the data is zero, coefficient of variation cannot be computed.")

    cv = std_dev / mean
    return cv

# Example usage
data = [10, 20, 30, 40, 50]
cv = coefficient_of_variation(data)
print(f"Coefficient of Variation: {cv}")
