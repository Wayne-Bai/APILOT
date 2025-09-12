import numpy as np

# Function to calculate relative z-scores
def calculate_relative_zscores(data_points, reference_point):
    """
    Calculate the relative z-scores for a list of data points
    relative to a reference point.

    Args:
        data_points (list): List of data points.
        reference_point (float): Reference point to calculate z-scores.

    Returns:
        list: List of z-scores.
    """
    # Calculate the mean of the data points (excluding the reference point)
    mean = np.mean([point for i, point in enumerate(data_points) if i!= np.argmin(np.abs(np.array(data_points) - reference_point))])

    # Calculate the standard deviation of the data points (excluding the reference point)
    std_dev = np.std([point for i, point in enumerate(data_points) if i!= np.argmin(np.abs(np.array(data_points) - reference_point))])

    # Calculate the relative z-scores
    relative_zscores = [(point - mean) / std_dev for point in data_points]

    return relative_zscores

# Example usage:
data_points = [10, 15, 12, 18, 20]
reference_point = 15

relative_z_scores = calculate_relative_zscores(data_points, reference_point)
print(relative_z_scores)
