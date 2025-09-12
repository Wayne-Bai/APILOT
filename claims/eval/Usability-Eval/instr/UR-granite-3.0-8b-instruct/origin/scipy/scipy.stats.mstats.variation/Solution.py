import numpy as np
from scipy.stats import variation

def compute_coefficient_of_variation(data):
    """
    Compute the coefficient of variation for a given dataset.

    Parameters:
    data (list or numpy array): The dataset for which the coefficient of variation is to be computed.

    Returns:
    float: The coefficient of variation.
    """
    # Calculate the mean of the dataset
    mean = np.mean(data)

    # Calculate the standard deviation of the dataset
    std_dev = np.std(data)

    # Compute the coefficient of variation
    cv = std_dev / mean

    return cv
