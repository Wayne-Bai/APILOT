import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import make_classification
from sklearn.svm import SVC

# Generate a binary classification problem with 100 samples and 2 features
X, y = make_classification(n_samples=100, n_features=2, random_state=42)

# Train a SVM classifier
clf = SVC(random_state=42)
clf.fit(X, y)

# Compute true and predicted probabilities for a calibration curve
prob_true, prob_pred = calibration_curve(y, clf.predict_proba(X)[:, 1], n_bins=10)

# Train a CalibratedClassifierCV with the SVM classifier
clf_cal = CalibratedClassifierCV(clf, cv=3)
clf_cal.fit(X, y)

# Compute true and predicted probabilities for the calibrated classifier
prob_true_cal, prob_pred_cal = calibration_curve(y, clf_cal.predict_proba(X)[:, 1], n_bins=10)