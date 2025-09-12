# Import necessary libraries
import scipy.stats as stats
import numpy as np

def calculate_z_scores(data):
    """
    Calculate the relative z-scores.

    Args:
    data (list): A list of numbers.

    Returns:
    list: A list of z-scores.
    """
    # Calculate the mean of the data
    mean = np.mean(data)

    # Calculate the standard deviation of the data
    std_dev = np.std(data)

    # Calculate the z-scores
    z_scores = [(x - mean) / std_dev for x in data]

    return z_scores

def calculate_z_scores_scipy(data):
    """
    Calculate the relative z-scores using scipy.

    Args:
    data (list): A list of numbers.

    Returns:
    list: A list of z-scores.
    """
    # Calculate the z-scores
    z_scores = stats.zscore(data)

    return z_scores

# Example usage
data = [1, 2, 3, 4, 5]
print("Data:", data)

print("Calculate z-scores manually:")
print(calculate_z_scores(data))

print("Calculate z-scores using scipy:")
print(calculate_z_scores_scipy(data))
