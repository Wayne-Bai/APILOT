import scipy.stats as stats
import numpy as np

def calculate_relative_z_scores(data):
    """
    Calculate the relative z-scores for a given dataset.

    Parameters:
    data (list or numpy array): The input dataset.

    Returns:
    relative_z_scores (list): A list of relative z-scores.
    """
    # Calculate the mean of the dataset
    mean = np.mean(data)

    # Calculate the standard deviation of the dataset
    std_dev = np.std(data)

    # Calculate the relative z-scores
    relative_z_scores = [(x - mean) / std_dev for x in data]

    return relative_z_scores

# Example usage
data = [10, 15, 12, 18, 20, 22, 19, 17, 16, 14]
relative_z_scores = calculate_relative_z_scores(data)

print("Relative z-scores:")
for i, score in enumerate(relative_z_scores):
    print(f"Data point {i+1}: {score:.4f}")

# Alternatively, you can use scipy's zscore function
data = np.array([10, 15, 12, 18, 20, 22, 19, 17, 16, 14])
relative_z_scores_scipy = stats.zscore(data)

print("\nRelative z-scores using scipy:")
for i, score in enumerate(relative_z_scores_scipy):
    print(f"Data point {i+1}: {score:.4f}")
