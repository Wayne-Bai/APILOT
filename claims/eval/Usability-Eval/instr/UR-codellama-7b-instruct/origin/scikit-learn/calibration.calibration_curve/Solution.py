
import numpy as np
from sklearn.calibration import CalibratedClassifierCV

# Define the number of bins for the calibration curve
bins = 5

# Generate synthetic data for demonstration purposes
X = np.random.rand(100, 10)
y = np.random.randint(0, 2, size=100)

# Define a binary classifier using scikit-learn's LogisticRegression
clf = CalibratedClassifierCV(base_estimator=LogisticRegression(), n_bins=bins)

# Fit the classifier to the data
clf.fit(X, y)

# Compute true and predicted probabilities for a calibration curve
true_probs = clf.predict_proba(X)[:, 1]
pred_probs = clf.calibration_curve(X)

# Plot the calibration curve
import matplotlib.pyplot as plt
plt.plot(true_probs, pred_probs, 'o-')
plt.xlabel('True probability')
plt.ylabel('Predicted probability')
plt.title('Calibration Curve')
plt.show()
