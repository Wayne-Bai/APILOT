
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.datasets import make_classification

# Generate some example data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Fit a calibrated classifier using isotonic regression
calibrated_isotonic = CalibratedClassifierCV(base_estimator=lr, method='isotonic', cv='prefit')
calibrated_isotonic.fit(X_test, y_test)

# Fit a calibrated classifier using logistic regression
calibrated_logistic = CalibratedClassifierCV(base_estimator=lr, method='sigmoid', cv='prefit')
calibrated_logistic.fit(X_test, y_test)

# Evaluate the calibrated classifiers
y_proba_isotonic = calibrated_isotonic.predict_proba(X_test)
y_proba_logistic = calibrated_logistic.predict_proba(X_test)

print("Isotonic Calibration Log Loss:", log_loss(y_test, y_proba_isotonic))
print("Logistic Calibration Log Loss:", log_loss(y_test, y_proba_logistic))
