from sklearn.metrics import calibration_curve
import numpy as np
import matplotlib.pyplot as plt

# Assuming y_true are the true labels and y_prob are the predicted probabilities
y_true = np.array([0, 0, 1, 1, 0, 1, 0, 1, 1, 0])
y_prob = np.array([0.1, 0.4, 0.7, 0.9, 0.2, 0.8, 0.3, 0.6, 0.5, 0.1])

# Compute true and predicted probabilities
frac_of_positives, mean_predicted_value = calibration_curve(y_true, y_prob, n_bins=10)

# Plot calibration curve
plt.plot(mean_predicted_value, frac_of_positives, "s-")
plt.xlabel("Mean predicted value")
plt.ylabel("Fraction of positives")
plt.title("Calibration curve")
plt.show()
