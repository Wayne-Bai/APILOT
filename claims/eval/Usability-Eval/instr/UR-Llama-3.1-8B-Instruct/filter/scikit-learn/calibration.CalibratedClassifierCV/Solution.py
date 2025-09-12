# Import necessary libraries
from sklearn.calibration import calibration_curve
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
n_samples = 1000
n_features = 10
X = np.random.rand(n_samples, n_features)
y = (X[:, 0] > 0.5).astype(int)  # Binary classification

# Get the posterior probabilities from the logistic regression model
lr = LogisticRegression()
lr.fit(X, y)
y_pred_proba = lr.predict_proba(X)[:, 1]

# Plot the calibration curve for logistic regression
plt.figure(figsize=(8, 6))
fraction_of_positives, mean_predicted_value = calibration_curve(y, y_pred_proba, n_bins=10)
plt.plot(mean_predicted_value, fraction_of_positives,'s-', label='Logistic Regression')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Mean Predicted Probability')
plt.ylabel('Fraction of Positive Samples')
plt.title('Calibration Curve')
plt.show()

# Use isotonic regression to calibrate the posterior probabilities
ir = IsotonicRegression(out_of_bounds='clip')
ir.fit(mean_predicted_value.reshape(-1, 1), fraction_of_positives)

# Plot the calibration curve for isotonic regression
y_pred_proba_calibrated = ir.predict(mean_predicted_value.reshape(-1, 1)).flatten()
plt.figure(figsize=(8, 6))
fraction_of_positives_calibrated, _ = calibration_curve(y, y_pred_proba_calibrated, n_bins=10)
plt.plot(mean_predicted_value, fraction_of_positives_calibrated,'s-', label='Isotonic Regression')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Mean Predicted Probability')
plt.ylabel('Fraction of Positive Samples')
plt.title('Calibration Curve')
plt.show()
