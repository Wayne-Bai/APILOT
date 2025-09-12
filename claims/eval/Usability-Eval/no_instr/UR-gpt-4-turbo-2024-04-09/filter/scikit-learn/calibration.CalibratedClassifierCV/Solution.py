import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss

# Generate synthetic data
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Calibrate model on the validation set using isotonic regression
calibrated_iso = CalibratedClassifierCV(base_estimator=rf, method='isotonic', cv='prefit')
calibrated_iso.fit(X_test, y_test)

# Calibrate model on the validation set using logistic regression
calibrated_log = CalibratedClassifierCV(base_estimator=rf, method='sigmoid', cv='prefit')
calibrated_log.fit(X_test, y_test)

# Predict probabilities
prob_iso = calibrated_iso.predict_proba(X_test)[:, 1]
prob_log = calibrated_log.predict_proba(X_test)[:, 1]

# Evaluate performance
brier_score_iso = brier_score_loss(y_test, prob_iso)
brier_score_log = brier_score_loss(y_test, prob_log)

print("Brier score with isotonic calibration:", brier_score_iso)
print("Brier score with logistic calibration:", brier_score_log)
