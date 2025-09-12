import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression

# Generate a 2D dataset
X, y = make_blobs(n_samples=100, n_features=2, centers=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Implement a Logistic Regression classifier
clf = LogisticRegression(max_iter=10000)

# Calibrating the classifier
calibration = CalibratedClassifierCV(base_estimator=clf)

# Fit the calibrated classifier
calibration.fit(X_train, y_train)

# Predict probabilities
prob_predicted = calibration.predict_proba(X_test)[:, 1]

# Evaluate classifier on test data, and compute true probabilities
y_pred = calibration.predict(X_test)

# Convert predicted quotients to probabilities
true_probabilities = prob_predicted
