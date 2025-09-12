
import numpy as np
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

# Generate some example data
y_true = np.array([0, 0, 1, 1])
y_prob = np.array([0.1, 0.2, 0.8, 0.9])

# Compute true and predicted probabilities for the calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=3, strategy='uniform')

# Plot the calibration curve
plt.plot(prob_pred, prob_true, marker='o')
plt.xlabel('Predicted Probability')
plt.ylabel('True Probability')
plt.title('Calibration Curve')
plt.show()
