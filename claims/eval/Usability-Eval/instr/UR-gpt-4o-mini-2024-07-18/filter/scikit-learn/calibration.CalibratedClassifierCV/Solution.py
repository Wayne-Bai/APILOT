import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a base classifier
base_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Create a calibrated classifier using isotonic regression
calibrated_clf = CalibratedClassifierCV(base_clf, method='isotonic', cv='prefit')

# Fit the base classifier on data
base_clf.fit(X_train, y_train)

# Fit the calibrated classifier
calibrated_clf.fit(X_train, y_train)

# Now you can use calibrated_clf to predict probabilities
probabilities = calibrated_clf.predict_proba(X_test)
