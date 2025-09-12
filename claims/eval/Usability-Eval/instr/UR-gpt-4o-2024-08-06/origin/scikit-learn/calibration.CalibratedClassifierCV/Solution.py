from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss
import numpy as np

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a logistic regression model
clf = LogisticRegression()

# Fit the logistic regression model
clf.fit(X_train, y_train)

# Calibrate the probabilities with isotonic regression
calibrated_clf_isotonic = CalibratedClassifierCV(base_estimator=clf, method='isotonic', cv='prefit')
calibrated_clf_isotonic.fit(X_train, y_train)

# Calibrate the probabilities with logistic regression (Platt scaling)
calibrated_clf_sigmoid = CalibratedClassifierCV(base_estimator=clf, method='sigmoid', cv='prefit')
calibrated_clf_sigmoid.fit(X_train, y_train)

# Predict the probabilities
prob_pos_isotonic = calibrated_clf_isotonic.predict_proba(X_test)[:, 1]
prob_pos_sigmoid = calibrated_clf_sigmoid.predict_proba(X_test)[:, 1]
prob_pos_unreliable = clf.predict_proba(X_test)[:, 1]

# Calculate Brier scores
brier_score_unreliable = brier_score_loss(y_test, prob_pos_unreliable)
brier_score_isotonic = brier_score_loss(y_test, prob_pos_isotonic)
brier_score_sigmoid = brier_score_loss(y_test, prob_pos_sigmoid)

print(f"Brier score (unreliable): {brier_score_unreliable:.3f}")
print(f"Brier score (isotonic): {brier_score_isotonic:.3f}")
print(f"Brier score (sigmoid): {brier_score_sigmoid:.3f}")
