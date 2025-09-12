import numpy as np
from sklearn.metrics import calibration_curve

# Assuming y_true are the true binary labels and y_probs are the predicted probabilities
y_true = np.array([0, 0, 1, 1, 0, 1, 1])  # Example true labels
y_probs = np.array([0.1, 0.4, 0.35, 0.8, 0.7, 0.9, 0.95])  # Example predicted probabilities

# Compute true and predicted probabilities for a calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_probs, n_bins=5)

# Output the results
print("True probabilities:", prob_true)
print("Predicted probabilities:", prob_pred)
