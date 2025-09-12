from sklearn.calibration import calibration_curve
from sklearn.metrics import plot_calibration_curve
import matplotlib.pyplot as plt
import numpy as np

# Assume X_test and y_test are your test data and labels
# X_test = ...
# y_test = ...

# Assuming clf is your trained binary classifier
# clf = ...

# Compute true and predicted probabilities
y_prob = clf.predict_proba(X_test)[:, 1]
y_true = y_test

# Compute the calibration curve
fraction_of_positives, mean_predicted_value = calibration_curve(y_true, y_prob, n_bins=10)

# Plot the calibration curve
plt.plot(mean_predicted_value, fraction_of_positives, "s-")
plt.plot(np.linspace(0, 1, 100), np.linspace(0, 1, 100), "k--")
plt.xlabel("Mean predicted value")
plt.ylabel("Fraction of positives")
plt.title("Calibration curve")
plt.show()
