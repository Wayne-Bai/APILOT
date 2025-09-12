import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

# Generate some data for illustration
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])

# Compute true and predicted probabilities for a calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_scores, n_bins=10)

# Plot the calibration curve
plt.figure(figsize=(6, 6))
plt.plot(prob_pred, prob_true, marker='.', label='Data')
plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='Perfect Calibration')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('Predicted Probability')
plt.ylabel('True Probability')
plt.legend()
plt.show()
