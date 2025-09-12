from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import make_classification
from sklearn.svm import SVC
import numpy as np

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                           n_redundant=5, random_state=42)

# Train a support vector machine (SVM) classifier
clf = SVC(random_state=42)
clf.fit(X, y)

# Compute true and predicted probabilities for a calibration curve
calibrated_clf = CalibratedClassifierCV(clf, cv=5)
calibrated_clf.fit(X, y)

probabilities = calibrated_clf.predict_proba(X)[:, 1]
