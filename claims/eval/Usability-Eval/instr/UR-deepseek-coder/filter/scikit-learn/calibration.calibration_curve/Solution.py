import numpy as np
from sklearn.metrics import brier_score_loss
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

def compute_calibration_curve(y_true, y_pred_probs, n_bins=10):
    # Compute the calibration curve
    prob_true, prob_pred = calibration_curve(y_true, y_pred_probs, n_bins=n_bins)
    
    # Compute the Brier score
    brier_score = brier_score_loss(y_true, y_pred_probs)
    
    return prob_true, prob_pred, brier_score

# Example usage
y_true = np.array([0, 0, 1, 1])
y_pred_probs = np.array([0.1, 0.4, 0.35, 0.8])

prob_true, prob_pred, brier_score = compute_calibration_curve(y_true, y_pred_probs)

print("Calibration Curve - True Probabilities:", prob_true)
print("Calibration Curve - Predicted Probabilities:", prob_pred)
print("Brier Score:", brier_score)

# Plotting the calibration curve
plt.figure(figsize=(10, 10))
plt.plot(prob_pred, prob_true, marker='o', linestyle='--', label='Calibration Curve')
plt.plot([0, 1], [0, 1], linestyle='--', label='Perfectly Calibrated')
plt.xlabel("Predicted Probability")
plt.ylabel("True Probability")
plt.title("Calibration Curve")
plt.legend()
plt.show()
