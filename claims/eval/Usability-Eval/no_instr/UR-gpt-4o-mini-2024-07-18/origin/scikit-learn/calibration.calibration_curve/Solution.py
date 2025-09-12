import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve

# Generate some sample binary classifier probabilities and true labels
# Replace these with your actual model's predicted probabilities and true labels
y_true = np.random.randint(0, 2, size=1000)  # True binary labels
y_prob = np.random.rand(1000)  # Predicted probabilities from a binary classifier

# Compute the calibration curve
prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=10)

# Plotting the calibration curve
plt.figure(figsize=(10, 6))
plt.plot(prob_pred, prob_true, marker='o', label='Calibration Curve')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Perfectly calibrated')
plt.xlabel('Mean predicted probability')
plt.ylabel('Fraction of positives')
plt.title('Calibration Curve')
plt.legend()
plt.show()
