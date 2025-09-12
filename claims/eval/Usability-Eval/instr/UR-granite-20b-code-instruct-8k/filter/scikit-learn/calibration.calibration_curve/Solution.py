import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import calibration_curve

# Generate some data for classification
X, y = datasets.make_classification(n_samples=10000, n_features=20,
n_informative=2, n_redundant=10, random_state=42)

# Train a logistic regression model
clf = linear_model.LogisticRegression()
clf.fit(X, y)

# Generate probabilities of the positive class
y_pred_prob = clf.predict_proba(X)[:, 1]

# Compute the calibration curve
bins = np.arange(0, 1.05, 0.05)
frac_of_positives, mean_predicted_value = calibration_curve(y, y_pred_prob, n_bins=10)

# Plot the calibration curve
plt.plot(mean_predicted_value, frac_of_positives, 'o-')
plt.show()
