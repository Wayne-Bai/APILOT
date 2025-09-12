# Import necessary libraries
from sklearn.calibration import calibration_curve
import numpy as np

# Define a function to compute true and predicted probabilities
def compute_calibration_curve(y_true, y_pred_proba):
    """
    Compute true and predicted probabilities for a calibration curve.

    Parameters:
    y_true (numpy array): Ground truth labels.
    y_pred_proba (numpy array): Predicted probabilities.

    Returns:
    fractions_of_positives, mean_predicted_value: Arrays to plot the calibration curve.
    """
    # Discretize the [0, 1] interval into bins using quantiles
    n_bins = 5
    quantiles = np.hanning(n_bins)
    quantiles = quantiles / quantiles.sum()

    # Compute the true and predicted calibration curves
    fractions_of_positives, mean_predicted_value = calibration_curve(y_true=y_true, 
                                                                y_pred_proba=y_pred_proba, 
                                                                n_bins=n_bins)

    return fractions_of_positives, mean_predicted_value
