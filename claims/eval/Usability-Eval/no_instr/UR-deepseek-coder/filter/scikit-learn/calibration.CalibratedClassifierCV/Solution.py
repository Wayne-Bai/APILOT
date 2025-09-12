import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import brier_score_loss

# Generate a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Train a base classifier (Logistic Regression)
base_classifier = LogisticRegression()

# Calibrate using Isotonic Regression
calibrated_isotonic = CalibratedClassifierCV(base_classifier, method='isotonic')
calibrated_isotonic.fit(X_train, y_train)

# Calibrate using Logistic Regression
calibrated_logistic = CalibratedClassifierCV(base_classifier, method='sigmoid')
calibrated_logistic.fit(X_train, y_train)

# Predict probabilities on the test set
y_prob_isotonic = calibrated_isotonic.predict_proba(X_test)[:, 1]
y_prob_logistic = calibrated_logistic.predict_proba(X_test)[:, 1]

# Evaluate the Brier score loss
brier_isotonic = brier_score_loss(y_test, y_prob_isotonic)
brier_logistic = brier_score_loss(y_test, y_prob_logistic)

print(f"Brier score loss (Isotonic Regression): {brier_isotonic}")
print(f"Brier score loss (Logistic Regression): {brier_logistic}")
