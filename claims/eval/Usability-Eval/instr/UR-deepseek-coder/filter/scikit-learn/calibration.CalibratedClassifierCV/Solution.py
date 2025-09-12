import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression

# Generate a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a base classifier (e.g., SVM)
base_classifier = SVC(probability=True)

# Calibrate the classifier using isotonic regression
isotonic_calibrated_classifier = CalibratedClassifierCV(base_classifier, method='isotonic')
isotonic_calibrated_classifier.fit(X_train, y_train)

# Calibrate the classifier using logistic regression
logistic_calibrated_classifier = CalibratedClassifierCV(base_classifier, method='sigmoid')
logistic_calibrated_classifier.fit(X_train, y_train)

# Predict probabilities on the test set
isotonic_probs = isotonic_calibrated_classifier.predict_proba(X_test)[:, 1]
logistic_probs = logistic_calibrated_classifier.predict_proba(X_test)[:, 1]

# Print the calibrated probabilities
print("Isotonic Calibrated Probabilities:", isotonic_probs)
print("Logistic Calibrated Probabilities:", logistic_probs)
