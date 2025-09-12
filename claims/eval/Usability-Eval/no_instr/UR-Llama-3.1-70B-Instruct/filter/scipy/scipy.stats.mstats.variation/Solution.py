import numpy as np

def compute_coefficient_of_variation(data):
    """
    Compute the coefficient of variation.

    The coefficient of variation (CV) is a standardized measure of dispersion
    of a probability distribution or frequency distribution. It is the ratio
    of the standard deviation to the mean.

    CV = σ / μ

    Parameters:
    data (list or numpy.array): Input data.

    Returns:
    float: Coefficient of variation.
    """
    # Compute the mean of the data
    mean = np.mean(data)

    # Compute the standard deviation of the data
    std_dev = np.std(data)

    # Compute the coefficient of variation
    cv = std_dev / mean

    return cv


# Example usage
data = [1, 2, 3, 4, 5]
cv = compute_coefficient_of_variation(data)

print("Coefficient of variation: ", cv)
