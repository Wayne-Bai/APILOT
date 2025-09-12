import numpy as np
from sklearn.datasets import make_classification
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import calibration_curve

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred_prob = lr.predict_proba(X_test)[:, 1]

# Calculate the calibration curve
frac_pos, mean_prob = calibration_curve(y_test, y_pred_prob, n_bins=10)

# Plot the calibration curve
import matplotlib.pyplot as plt
plt.plot(mean_prob, frac_pos, 's-')
plt.xlabel('Mean predicted probability')
plt.ylabel('Fraction of positives')
plt.title('Calibration curve')
plt.show()
