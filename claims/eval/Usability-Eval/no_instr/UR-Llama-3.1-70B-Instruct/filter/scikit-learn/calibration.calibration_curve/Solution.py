# Import necessary libraries
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
np.random.seed(0)
y_true = np.random.randint(0, 2, size=1000)
y_pred = np.random.rand(1000)

# Compute true and predicted probabilities for a calibration curve
fraction_of_positives, mean_predicted_value = calibration_curve(y_true, y_pred, n_bins=10)

# Print the fraction of positives and the mean predicted value for each bin
for i in range(len(fraction_of_positives)):
    print(f"Fraction of positives in bin {i}: {fraction_of_positives[i]}")
    print(f"Mean predicted value in bin {i}: {mean_predicted_value[i]}")

# Plot the calibration curve
plt.plot(mean_predicted_value, fraction_of_positives,'s-', label='Calibration Curve')
plt.plot([0, 1], [0, 1], 'k:', label='Perfectly Calibrated')
plt.xlabel('Mean Predicted Value')
plt.ylabel('Fraction of Positives')
plt.title('Calibration Curve')
plt.legend()
plt.show()
